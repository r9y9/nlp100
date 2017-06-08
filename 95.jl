using StatsBase

for path in ["94.jl.85.out", "94.jl.90.out"]
    X = readcsv(path)
    N = size(X,1)

    C = corspearman(map(Float64,X[:,3]), map(Float64, X[:,4]))
    println("Spearman correlation for $path: $C")

    v1 = map(Float64,X[:,3])
    v2 = map(Float64,X[:,4])
    r1 = similar(v1)
    r2 = similar(v2)

    r1[sortperm(v1)] = 1:N
    r2[sortperm(v2)] = 1:N

    C = 1 - 6*sum((r1 - r2).*(r1 - r2)) / (N^3-N)
    println("(manual computation) Spearman correlation for $path: $C")
end
