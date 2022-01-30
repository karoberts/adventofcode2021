(load-file "utils.clj")

(def fish
  (map
    utils/parseInt
    (clojure.string/split (first (utils/read-lines "6.txt")) #",")))

;(def fish [3 4 3 1 2])

(def counts 
  (-> {}
    (into (for [x (range 9)] [x 0]))
    (merge (frequencies fish))))

(defn simulate
  ([day counts] (simulate day counts nil))
  ([day counts day80]
    (if (= day 256)
      {:80 day80 :256 (reduce + (vals counts))}
      (let [zeros (counts 0)]
        (recur
          (inc day)
          (-> {}
            (into (for [x (range 8)] [x (counts (inc x))]))
            (assoc 6 (+ (counts 7) zeros))
            (assoc 8 zeros))
          (if (= day 80)
            (reduce + (vals counts))
            day80))))))

(def answers (simulate 0 counts))
(println "part1" (answers :80))
(println "part2" (answers :256))