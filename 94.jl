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

combined = readcsv("combined.csv")[2:end,:]

for idx in 1:size(combined,1)
    word1, word2, score = combined[idx,:]

    D = -1
    try
        v1 = X[vocab2idx[lowercase(word1)],:]
        v2 = X[vocab2idx[lowercase(word2)],:]
        D = dot(v1, v2) / norm(v1) / norm(v2)
        isnan(D) && (D = 0)
    catch e
        if isa(e, KeyError)
            D = 01
        else
            rethrow(e)
        end
    end

    println("$word1,$word2,$score,$D")
end
