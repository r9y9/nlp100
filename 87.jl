using JLD

jldopen("85.jld") do file
    global X, vocab, vocab2idx, idx2vocab
    X = read(file, "X")
    vocab = read(file, "vocab")
    vocab2idx = read(file, "vocab2idx")
    idx2vocab = read(file, "idx2vocab")
end


x1 = X[vocab2idx["united_states"],:]
x2 = X[vocab2idx["u.s"],:]

using Distances
@show cosine_dist(x1, x2)
