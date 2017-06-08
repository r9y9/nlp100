countries = readcsv("countries.csv")
splitted_names = filter(x -> length(x) > 0, split.(countries[2:end,2]))
splitted_names = map(x -> lowercase.(x), splitted_names)

open("80.py.out") do f
    for line in readlines(f)
        if length(line) < 1
            continue
        end
        words = filter(x -> !isempty(x), lowercase.(split(line[1:end])))
        newwords = String[]
        idx = 1
        while idx < length(words)
            word = words[idx]
            found = false
            for c in splitted_names
                cl = length(c)
                if idx + cl - 1 >= length(words)
                    break
                end
                if length(c) > 1 && words[idx:idx+cl-1] == c
                    push!(newwords, join(c, "_"))
                    idx = idx + cl
                    found = true
                end
            end
            if !found
                idx += 1
                push!(newwords, word)
            end
        end

        words = newwords
        if length(words) > 0
            for token in words
                print(token, " ")
            end
            println("")
        end
    end
end
