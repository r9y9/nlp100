using JLD
using ProgressMeter

open("81.jl.out.vector") do f
    global nvocab, h

    nvocab, h = parse.(Int, split(readline(f)))
    global X = zeros(h, nvocab) # to be transposed later
    global vocab = Vector{String}(nvocab)

    @showprogress 1 "ahahaha" for (idx,line) in enumerate(readlines(f))
        s = split(line)
        word = s[1]
        fv = parse.(Float32, s[2:end])
        @assert length(fv) == h

        vocab[idx] = word
        X[:,idx] = fv
    end

    X = X'
    @assert size(X) == (nvocab, h)

    global vocab2idx = Dict()
    global idx2vocab = Dict()
    for (idx,word) in enumerate(vocab)
        vocab2idx[word] = idx
        idx2vocab[idx] = word
    end
end

if true
    jldopen("90.jld", "w") do file
        write(file, "X", X)
        write(file, "vocab", vocab)
        write(file, "vocab2idx", vocab2idx)
        write(file, "idx2vocab", idx2vocab)
    end
end
