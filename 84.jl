using ProgressMeter

ftc = Dict()
ft = Dict()
fc = Dict()
N = 0

open("82.jl.out") do f
    @showprogress 1 "ahaha" for line in readlines(f)
        global N, ftc,ft,fc
        words = filter(x -> !isempty(x), strip.(split(line)))
        words = filter(x -> x != "N/A", words)
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
end

vocab = unique(union(map(x->x[1], keys(ftc)),map(x->x[2], keys(ftc))))
vocab2idx = Dict()
for (idx,word) in enumerate(vocab)
    vocab2idx[word] = idx
end
# indices = collect(1:length(vocab))

Nv = length(vocab)

X = spzeros(Nv,Nv)
for ((t,c), v) in ftc
    tidx, cidx = vocab2idx[t],vocab2idx[c]
    if v > 10
        vv = max(log(N*v/(ft[t]*fc[c])), 0.0)
        X[tidx,cidx] = vv
    end
end

@show size(X)
