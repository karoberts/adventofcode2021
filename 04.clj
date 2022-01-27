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
            #(Integer/parseInt %)
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

(defn make-boards [boards]
  (mapv
    (fn[b] (apply conj #{} (flatten b)))
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

(defn check-winning-board [boards boardsets drawsSoFar draw]
  (if (empty? boards)
    nil
    (if (board-wins (first boards) drawsSoFar)
      [(first boards) (first boardsets) draw]
      (check-winning-board (rest boards) (rest boardsets) drawsSoFar draw))))

(defn find-winning-board [draws boards boardsets drawsSoFar prevDraw]
  (if-let [winner (check-winning-board boards boardsets drawsSoFar prevDraw)]
    winner
    (if (empty? draws)
      nil
      (find-winning-board
        (rest draws)
        boards
        (map #(disj %1 (first draws)) boardsets)
        (conj drawsSoFar (first draws))
        (first draws)))))

(defn calc-winning-board [board]
  (->> (first board)
    (flatten)
    (filter #(contains? (second board) %1))
    (reduce +)
    (* (nth board 2))))

(def lines (clojure.string/split-lines (slurp "4.txt")))

(def draws
  (map
    #(Integer/parseInt %)
    (clojure.string/split (first lines) #",")))

(def boards (parse-boards (drop 2 lines)))

(def winner (find-winning-board draws boards (make-boards boards) #{} -1))
(println "part1" (calc-winning-board winner))

(defn find-last-winning-board [draws boards boardsets drawsSoFar prevDraw lastWinner]
  (if (empty? draws)
    lastWinner
    (let [results (keep #(board-wins %1 drawsSoFar) boards)
          winners (->> results
            (map vector boards boardsets (repeat (count results) prevDraw))
            (filter #(%1 3)))]
      (find-last-winning-board
        (rest draws)
        (->> results
          (map vector boards)
          (filter #(not (%1 1)))
          (map #(%1 0)))
        (->> results
          (map vector boardsets)
          (filter #(not (%1 1)))
          (map #(%1 0))
          (map #(disj %1 (first draws))))
        (conj drawsSoFar (first draws))
        (first draws)
        (or (first winners) lastWinner)))))

(def lastWinner (find-last-winning-board draws boards (make-boards boards) #{} -1 nil))
(println "part2" (calc-winning-board lastWinner))