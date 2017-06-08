using JLD
using Distances


if !isdefined(:loaded) || !loaded
    println("Loading...")
    jldopen("85.jld") do file
        global X, vocab, vocab2idx, idx2vocab
        X = read(file, "X")
        vocab = read(file, "vocab")
        vocab2idx = read(file, "vocab2idx")
        idx2vocab = read(file, "idx2vocab")
        global loaded = true
    end
end


# note: depends some globals
function similar_words(word; v = nothing, K=10)
    if v === nothing
        v = X[vocab2idx[word],:]
    end
    distances = zeros(length(vocab))
    for i in 1:length(vocab)
        distances[i] = cosine_dist(v, X[i,:])
    end

    p = sortperm(distances)
    words = []
    for i in 1:K
        push!(words, (idx2vocab[p[i]], distances[p[i]]))
    end

    words
end


v1 = X[vocab2idx["spain"],:]
v2 = X[vocab2idx["madrid"],:]
v3 = X[vocab2idx["athens"],:]

v = v1 - v2 + v3

words = similar_words("Dummy", v = v, K=11)

for (idx, (word, score)) in enumerate(words)
    println("$idx: ($word, $score)")
end

#=
julia> @time include("./89.jl")
1: (Spain, 0.1298535311445519)
2: (Sweden, 0.15812807697715514)
3: (Italy, 0.15933862165878132)
4: (Germany, 0.18661154954426418)
5: (Austria, 0.19796824010990155)
6: (France, 0.199986843038379)
7: (Netherlands, 0.20552766319824411)
8: (Belgium, 0.22052314063678613)
9: (Denmark, 0.2216631629606418)
10: (Télévisions, 0.22247732061479797)
11: (Hungary, 0.2550573826225834)
  0.806980 seconds (2.53 M allocations: 1.045 GiB, 9.11% gc time)
=#

# ***90***
#=
julia> @time include("./89.jl")
1: (Spain, 0.3457379922084114)
2: (Greece, 0.4379238679036045)
3: (Sweden, 0.44022662117009537)
4: (Athens, 0.4428090455580942)
5: (Norway, 0.46073073622093297)
6: (Poland, 0.48033036303527465)
7: (Denmark, 0.4824352945520548)
8: (Netherlands, 0.4904862473474464)
9: (Turkey, 0.49091823018130454)
10: (Germany, 0.5010240875959475)
11: (Italy, 0.5093253306302299)
=#
