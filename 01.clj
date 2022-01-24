
; read file
(def lines 
  (map #(Integer/parseInt %)
    (clojure.string/split-lines (slurp "1.txt"))))

; reduce based
(defn do-part1-reduce []
  (second
    (reduce
      (fn [acc cur]
        (let [prev (acc 0)
              count (acc 1)]
          (if (= -1 prev)
            [cur count]
            [cur (if (> cur prev)
              (+ 1 count)
              count)]
          )))
      [-1 0]
      lines)))

(do-part1-reduce) ; jit warmup
(time (println "part1 (reduce)" (do-part1-reduce)))

; explicit recursion
(defn do-part1-recursion
  ([lines] (do-part1-recursion (rest lines) (first lines)))
  ([lines prev]
    (if (empty? lines)
      0
      (+ 
        (if (> (first lines) prev) 1 0)
        (do-part1-recursion
          (rest lines)
          (first lines))))))

(do-part1-recursion lines)
(time (println "part1 (explicit)" (do-part1-recursion lines)))
  
; recur
(defn do-part1-recur
  ([lines] (do-part1-recur (rest lines) (first lines) 0))
  ([lines prev count]
    (if (empty? lines)
      count
      (recur
       (rest lines)
       (first lines)
       (+ (if (> (first lines) prev) 1 0) count)))))

(do-part1-recur lines)
(time (println "part1 (recur)" (do-part1-recur lines)))

; count/filter/map
(defn part1-map []
  (count
    (filter 
      (fn [x] (< x 0))
      (map - lines (rest lines)))))

(part1-map)
(time (println "part1 (map)" (part1-map)))

;; part 2
(println)
(println "== Part 2 ==")

; explicit recursion
(defn do-part2-recursion
  ([lines] (do-part2-recursion (first lines) (second lines) (rest (rest lines)) Integer/MAX_VALUE))
  ([prev1 prev2 lines prev-win]
    (if (empty? lines)
      0
      (do
        (let [this-win (+ prev1 prev2 (first lines))]
          (+ 
            (if (> this-win prev-win) 1 0)
            (do-part2-recursion
              prev2
              (first lines)
              (rest lines)
              this-win)))))))

(do-part2-recursion lines)
(time (println "part2 (recursion)" (do-part2-recursion lines)))

; recur
(defn do-part2-recur
  ([lines] (do-part2-recur (first lines) (second lines) (rest (rest lines)) Integer/MAX_VALUE 0))
  ([prev1 prev2 lines prev-win count]
    (if (empty? lines)
      count
      (do
        (let [this-win (+ prev1 prev2 (first lines))]
          (recur
            prev2
            (first lines)
            (rest lines)
            this-win
            (+ (if (> this-win prev-win) 1 0) count)))))))

(do-part2-recur lines)
(time (println "part2 (recur)" (do-part2-recur lines)))

; count/filter/map
(defn do-part2-map [lines]
  (let [wins (map #(reduce + %1)
               (map vector lines (rest lines) (rest (rest lines))))]
    (count
      (filter 
        #(< %1 0)
        (map - wins (rest wins))))))

(do-part2-map lines)
(time (println "part2 (map)" (do-part2-map lines)))
