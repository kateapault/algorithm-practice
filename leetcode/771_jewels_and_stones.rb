# @param {String} j
# @param {String} s
# @return {Integer}
def num_jewels_in_stones(j, s)
    jewels = 0
    
    (0...s.size).each do |i|
       if j.include? s[i] 
           puts "YES"
          jewels += 1 
       else
           puts "I guess #{s[i]} isn't in #{j}"
       end
    end
    jewels
end