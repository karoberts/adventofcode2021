(load-file "utils.clj")

(def crabs
  (map
    utils/parseInt
    (clojure.string/split (first (utils/read-lines "7.txt")) #",")))
    
;(def crabs [16 1 2 0 4 2 7 1 2 14])

(defn- abs [n] (max n (-' n)))

(defn do-part1 [crabs]
  (apply min
    (let [mincrab (apply min crabs)
          maxcrab (apply max crabs)]
      (into []
        (for [c (range mincrab (inc maxcrab))]
          (->> crabs
            (map #(abs (- %1 c)))
            (reduce +)))))))

(defn do-part2 [crabs]
  (letfn [
    (calc [i x]
      (let [diff (abs (- x i))]
        (as-> (inc diff) $ 
          (* diff $)
          (quot $ 2))))]
    (apply min
      (let [mincrab (apply min crabs)
            maxcrab (apply max crabs)]
        (into []
          (for [c (range mincrab (inc maxcrab))]
            (->> crabs
              (map (partial calc c))
              (reduce +))))))))

(println "part1" (do-part1 crabs))
(println "part2" (do-part2 crabs))