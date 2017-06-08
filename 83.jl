using ProgressMeter

open("82.jl.out") do f
    ftc = Dict()
    ft = Dict()
    fc = Dict()
    N = 0
    @showprogress 1 "ahaha" for line in readlines(f)
        words = filter(x -> !isempty(x) && x != "N/A", strip.(split(line)))
        word, context = words[1], words[2:end]

        # f(t,c)
        for c in context
            t = (word, c)
            if t in keys(ftc)
                ftc[t] += 1
            else
                ftc[t] = 1
            end
        end

        # f(t,*)
        if word in keys(ft)
            ft[word] += 1
        else
            ft[word] = 1
        end

        # f(*.c)
        for c in context
            if c in keys(fc)
                fc[c] += 1
            else
                fc[c] = 1
            end
        end

        N += 1
    end

    @show N
end
