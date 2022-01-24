; read file
(def lines
  (map 
    (fn[line] 
      (let [cmd (clojure.string/split line #" ")
            num (Integer/parseInt (cmd 1))]
        [(cmd 0) num]))
    (clojure.string/split-lines (slurp "2.txt"))))

(defn do-part1 
  ([lines] (do-part1 lines 0 0))
  ([lines x d]
    (if (empty? lines)
      (* x d)
      (let [line (first lines)
            num (line 1)]
        (case (line 0)
          "forward" (recur (rest lines) (+ x num) d)
          "down" (recur (rest lines) x (+ d num))
          "up" (recur (rest lines) x (- d num)))))))

(do-part1 lines)
(time (println "part1" (do-part1 lines)))
  
(defn do-part2
  ([lines] (do-part2 lines 0 0 0))
  ([lines x d a]
    (if (empty? lines)
      (* x d)
      (let [line (first lines)
            num (line 1)]
        (case (line 0)
          "forward" (recur (rest lines) (+ x num) (+ d (* a num)) a)
          "down" (recur (rest lines) x d (+ a num))
          "up" (recur (rest lines) x d (- a num)))))))

(do-part2 lines)
(time (println "part2" (do-part2 lines)))