(load-file "utils.clj")

(def lines (utils/read-lines "10.txt"))

(def score_map {\) 3, \] 57, \} 1197, \> 25137})
(def open_map {\( \), \[ \], \{ \}, \< \>})
(def p2_score_map {\) 1, \] 2, \} 3, \> 4})

(defn get-points
  ([line] (get-points line []))
  ([line stack]
    (if (empty? line)
      [0 stack]
      (let [c (first line)]
        (if (contains? open_map c)
          (get-points (rest line) (conj stack c))
          (if (= (open_map (peek stack)) c)
            (get-points (rest line) (pop stack))
            [(score_map c) []]))))))

(defn find-scores [lines]
  (->> lines
    (map get-points)
    (map #(%1 0))
    (filter #(> %1 0))))

(defn find-incomplete [lines]
  (->> lines
    (map get-points)
    (map #(%1 1))
    (filter #(> (count %1) 0))))

(defn get-points-2 [inc]
  (reduce
    (fn[acc cur]
      (+ (p2_score_map (open_map cur)) (* acc 5)))
    0
    (reverse inc)))

(defn find-scores-2 [incomplete]
  (let [scores
    (->> incomplete
      (map get-points-2)
      (sort)
      (vec))]
    (nth scores (quot (count scores) 2))))

(def scores (find-scores lines))
(println "part1" (reduce + scores))

(def incomplete (find-incomplete lines))
(println "part2" (find-scores-2 incomplete))