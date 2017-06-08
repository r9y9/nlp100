function f(path)
    open(path) do f
        N = 0
        corrects = 0
        for line in readlines(f)
            tokens = split(line)
            if tokens[4] == tokens[5] && tokens[6] != -1
                corrects += 1
            end
            N += 1
        end

        println("Result for $path: ", corrects/N)
    end
end

f("92.jl.85.out")
f("92.jl.90.out")

#=
julia> @time include("./93.jl")
Result for 92.jl.85.out: 0.15019762845849802
Result for 92.jl.90.out: 0.2134387351778656
=#
