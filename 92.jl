using JLD
using Distances
using ProgressMeter

if !isdefined(:loaded) || !loaded
    #jldopen("90.jld") do file
    jldopen("85.jld") do file
        global X, vocab, vocab2idx, idx2vocab
        X = read(file, "X")
        vocab = read(file, "vocab")
        vocab2idx = read(file, "vocab2idx")
        idx2vocab = read(file, "idx2vocab")
        global loaded = true
    end

    # @show length(vocab)
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
        # 1 - d for consistency..
        push!(words, (idx2vocab[p[i]], 1 - distances[p[i]]))
    end

    words
end


open("91.jl.out") do f
    for line in readlines(f)
        words = split(line)

        (most_similar_word, score) = "n/a", -1
        try
            v1 = X[vocab2idx[words[2]],:]
            v2 = X[vocab2idx[words[1]],:]
            v3 = X[vocab2idx[words[3]],:]
            v = v1 - v2 + v3
            (most_similar_word, score) = similar_words("dummy", v = v, K=2)[2]
        catch e
            if isa(e, KeyError)
                most_similar_word = "n/a"
                score = -1
            else
                rethrow(e)
            end
        end
        println(line, " ", most_similar_word, " ", score)
    end
end
