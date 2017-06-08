using JLD
using Distances


if !isdefined(:loaded) || !loaded
    println("Loading...")
    # jldopen("85.jld") do file
    jldopen("90.jld") do file
        global X, vocab, vocab2idx, idx2vocab
        X = read(file, "X")
        vocab = read(file, "vocab")
        vocab2idx = read(file, "vocab2idx")
        idx2vocab = read(file, "idx2vocab")
        global loaded = true
    end
end


# note: depends some globals
function similar_words(word; K=10, should_lower=true)
    if should_lower
        word = lowercase(word)
    end
    v = X[vocab2idx[word],:]
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


words = similar_words("England", K=11)
# words = similar_words("Spain", K=11)

for (idx, (word, score)) in enumerate(words)
    println("$idx: ($word, $score)")
end

#=
julia> @time include("./88.jl")
1: (England, 0.0)
2: (Scotland, 0.3268883016363757)
3: (Wales, 0.3797738775963655)
4: (Australia, 0.38495262864152646)
5: (Italy, 0.4457559448475833)
6: (Ireland, 0.45570685913751796)
7: (France, 0.47124095457277393)
8: (Netherlands, 0.49150145114866073)
9: (Spain, 0.4923261574483986)
10: (match, 0.4996265985763505)
11: (New_Zealand, 0.5014242983908542)
  0.797475 seconds (2.53 M allocations: 1.045 GiB, 9.35% gc time)
=#


# **90**
#=
julia> @time include("./88.jl")
1: (England, 0.0)
2: (Scotland, 0.3663732399867812)
3: (T20, 0.45535642583910907)
4: (Wales, 0.46629287761514726)
5: (Coope, 0.4867497657715091)
6: (Yorkshire, 0.5259334960472704)
7: (Australia, 0.5301869440377063)
8: (Leeds, 0.5345024659948912)
9: (Cardiff, 0.5370676668547449)
10: (match, 0.5375962084158777)
11: (Liverpool, 0.5377926492053353)
  0.593390 seconds (632.09 k allocations: 221.208 MiB, 20.46% gc time)
=#
