; Penyelesaian persoalan Partisi Bilangan bulat dengan Memoization

(def part
    (memoize
        (fn [[a b]]
            (cond 
              (or (< a 0) (< b 1)) 0
              (or (< a 2) (= b 1)) 1
              :else (+' (part [(- a b) b]) (part [a (dec b)]))))))
(defn integerPartition [n] (part [n n]))

(time (println (integerPartition 200)))
