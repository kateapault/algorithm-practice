def reverse(x)
    if x < 0
        n = x.abs.to_s.reverse.to_i
        if n > 2 ** 31
            n = 0
        end
        n *= -1
    else
        n = x.to_s.reverse.to_i
        if n > 2 ** 31
            n = 0
        end
    end
    n
end