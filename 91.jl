open("questions-words.txt") do f
    enter = false
    leave = false
    global r = []
    for line in readlines(f)
        words = split(line)
        if leave
            break
        end
        if words[1] != ":" && !enter
            continue
        end
        if words[1] == ":" && words[2] == "family"
            enter = true
            continue
        end
        if enter && !leave && words[1] == ":"
            leave = true
        end
        if enter && !leave
            push!(r, line)
        end
    end

    for v in r
        println(v)
    end
end
