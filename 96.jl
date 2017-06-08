countries = readcsv("countries.csv")
names = filter(x -> length(x) > 0, replace.(lowercase.(countries[2:end,2]), " ", "_"))

if !isdefined(:loaded) || !loaded
    jldopen("90.jld") do file
    # jldopen("85.jld") do file
        global X, vocab, vocab2idx, idx2vocab
        X = read(file, "X")
        vocab = read(file, "vocab")
        vocab2idx = read(file, "vocab2idx")
        idx2vocab = read(file, "idx2vocab")
        global loaded = true
    end

    # @show length(vocab)
end

# note: transpoed
X_c = zeros(size(X, 2), length(names))
total_missing = 0
for (i, name) in enumerate(names)
    try
        idx = vocab2idx[name]
        X_c[:,i] = X[idx,:]
    catch e
        if isa(e, KeyError)
            warn("key $name not found in vocab")
            total_missing += 1
        else
            rethrow(e)
        end
    end
end
if total_missing > 0
    warn("Missing $total_missing")
end

size(X_c)

using HDF5
h5open("96.jl.h5", "w") do f
    write(f, "X", X_c)
end
