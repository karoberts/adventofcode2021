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

(defn check-winning-board [boards boardsets drawsSoFar draw]
  (if (empty? boards)
    nil
    (if (some identity
          (map
            (fn[row] (every? #(contains? drawsSoFar %1) row))
            (first boards)))
      [(first boards) (first boardsets) draw]
      (let [cols (get-columns (first boards) 0)]
        (if (some boolean
              (map
                (fn[row] (every? #(contains? drawsSoFar %1) row))
                cols))
          [(first boards) (first boardsets) draw]
          (check-winning-board (rest boards) (rest boardsets) drawsSoFar draw))))))

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

