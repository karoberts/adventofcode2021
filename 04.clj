(load-file "utils.clj")

(defn parse-board
  ([lines] (parse-board lines 0 []))
  ([lines y board]
    (if (= y 5)
      board
      (parse-board 
        (rest lines)
        (inc y)
        (conj 
          board
          (mapv
            utils/parseInt
            (clojure.string/split (clojure.string/trim (first lines)) #"\s+")))))))

(defn parse-boards
  ([lines] (parse-boards lines []))
  ([lines boards]
    (if (empty? lines)
      boards
      (parse-boards
        (drop 6 lines)
        (conj
          boards
          (parse-board lines))))))

(defn print-boards [boards]
  (doseq [b boards]
    (doseq [r b]
      (print r)
      (newline))
    (newline)))

(defn make-boards-obj [boards]
  (mapv
    (fn[b] {
      :board b
      :unselected (apply conj #{} (flatten b)) })
    boards))

(defn get-columns [board col]
  (if (= col 5)
    []
    (conj 
      (get-columns board (inc col))
      (map #(nth %1 col) board))))

(defn board-wins [board drawsSoFar]
  (if (some identity
        (map
          (fn[row] (every? #(contains? drawsSoFar %1) row))
          board))
    true
    (let [cols (get-columns board 0)]
      (if (some boolean
            (map
              (fn[row] (every? #(contains? drawsSoFar %1) row))
              cols))
        true
        false))))

(defn calc-winning-board [board draw]
  (->> (board :board)
    (flatten)
    (filter #(contains? (board :unselected) %1))
    (reduce +)
    (* draw)))

(defn find-last-winning-board [draws boards drawsSoFar prevDraw firstWinner lastWinner]
  (if (empty? draws)
    [firstWinner lastWinner]
    (let [results (keep #(board-wins (%1 :board) drawsSoFar) boards)
          winners (->> results
            (map vector boards (repeat (count results) prevDraw))
            (filter #(%1 2)))]
      (find-last-winning-board
        (rest draws)
        (->> results
          (map vector boards)
          (filter #(not (%1 1)))
          (map (fn[b] 
            (update (b 0) :unselected disj (first draws)))))
        (conj drawsSoFar (first draws))
        (first draws)
        (or firstWinner (first winners))
        (or (first winners) lastWinner)))))

; main

(def lines (utils/read-lines "4.txt"))

(def draws
  (map
    utils/parseInt
    (clojure.string/split (first lines) #",")))

(def boards (parse-boards (drop 2 lines)))

(def winners (find-last-winning-board draws (make-boards-obj boards) #{} -1 nil nil))
(def firstWinner (winners 0))
(def lastWinner (winners 1))
(println "part1" (calc-winning-board (firstWinner 0) (firstWinner 1)))
(println "part2" (calc-winning-board (lastWinner 0) (lastWinner 1)))