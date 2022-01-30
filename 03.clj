(load-file "utils.clj")

; read file
(def lines (utils/read-lines-map-split "3.txt" utils/parseInt))

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

(defn count-bits-pos
  ([lines pos] (count-bits-pos lines pos 0))
  ([lines pos count]
    (if (empty? lines)
      count
      (count-bits-pos
        (rest lines)
        pos
        (+ count (nth (first lines) pos))))))

(defn filter-by-bits [lines pos bitval]
  (filter 
    #(= (nth %1 pos) bitval)
    lines))

(defn most-common [bitcount ct]
  (if (= (rem ct 2) 0)
    (if (>= bitcount (quot ct 2)) 1 0)
    (if (> bitcount (quot ct 2)) 1 0)))

(defn least-common [bitcount ct]
  (if (= (rem ct 2) 0)
    (if (>= bitcount (quot ct 2)) 0 1)
    (if (<= bitcount (quot ct 2)) 1 0)))

(defn do-part-2 [lines pos len tgt]
  (if (or (= pos (dec len)) (= 1 (count lines)))
    (vec (first lines))
    (let [bitcount (count-bits-pos lines pos)
          ct (count lines)
          mostcommon (most-common bitcount ct)
          leastcommon (least-common bitcount ct)]
      (do-part-2
        (filter-by-bits lines pos (if (= tgt 1) mostcommon leastcommon))
        (inc pos)
        len
        tgt))))
  
(time
  (do
    (def r3_2a (do-part-2 lines 0 (r1 1) 1))
    (def r3_2a2 (compute-binary r3_2a))

    (def r3_2b (do-part-2 lines 0 (r1 1) 0))
    (def r3_2b2 (compute-binary r3_2b))))

(println "part2" (* r3_2a2 r3_2b2))