D = 5

open("81.jl.out") do f
  for line in readlines(f)
    words = filter(x-> !isempty(x), strip.(split(line)))
    nw = length(words)
    for idx in 1:length(words)
      randd = rand(1:D)
      d = min(D, max(idx-1,1), nw-idx)
      print(words[idx], "\t")
      for i in -d:d
        i == 0 && continue
        if idx+i < 1 || idx+i > nw
          print("N/A\t")
        else
          print(words[idx+i], "\t")
        end
      end
      println()
    end
  end
end
