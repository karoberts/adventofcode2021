; read file
(def lines
  (map
    (fn[line] 
      (map 
        #(Integer/parseInt %)
        (clojure.string/split line #"")))
    (clojure.string/split-lines (slurp "3.txt"))))

(defn count-bits
  ([lines] 
    (count-bits
      lines 
      (vec 
        (replicate (count (first lines)) 0))
      0))
  ([lines counts count]
    (if (empty? lines)
      [counts count]
      (count-bits
        (rest lines)
        (map + (first lines) counts)
        (inc count)))))

(defn produce-num [bits count t f]
  (let [half (quot count 2)]
    (mapv #(if %1 t f)
      (map (fn[b] (> b half)) bits))))
    
(defn compute-binary
  ([bits] (compute-binary (rseq bits) 1))
  ([bits factor]
    (if (empty? bits)
      0
      (+ 
        (* factor (first bits))
        (compute-binary (rest bits) (* factor 2))))))

(time
  (do
    (def r1 (count-bits lines))
    (def r2a (produce-num (r1 0) (r1 1) 1 0))
    (def r2b (produce-num (r1 0) (r1 1) 0 1))
    (def r3a (compute-binary r2a))
    (def r3b (compute-binary r2b))))

(println "part1" (* r3a r3b))

