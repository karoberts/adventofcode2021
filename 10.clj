(def lines (clojure.string/split-lines (slurp "10.txt")))

(def score_map {\) 3, \] 57, \} 1197, \> 25137})
(def open_map {\( \), \[ \], \{ \}, \< \>})

(defn get-points
  ([line] (get-points line []))
  ([line stack]
    (if (empty? line)
      0
      (let [c (first line)]
        (if (contains? open_map c)
          (get-points (rest line) (conj stack c))
          (if (= (open_map (peek stack)) c)
            (get-points (rest line) (pop stack))
            (score_map c)))))))

(defn find-scores [lines]
  (map
    get-points
    lines))

(def scores (find-scores lines))
(println "part1" (reduce + scores))