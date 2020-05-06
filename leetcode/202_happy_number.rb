# @param {Integer} n
# @return {Boolean}
def is_happy(n)
    puts "HEY RUNNING"
    counter = 0
    until n == 1 || counter > 100
        puts "CYCLING"
        n_arr = n.to_s.split('')
        n = n_arr.reduce(0) {|x,y| x.to_i + y.to_i**2}
        puts "#{n_arr} squared adds up to #{n}"
        counter += 1
    end
    if counter > 100
        return false
    else
        return true
    end
end

is_happy(19)