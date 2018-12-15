use std::collections::HashMap;

#[aoc(day2, part1)]
pub fn part1(input: &str) -> usize {
    let twos=count_similar(input,2);
    let threes=count_similar(input,3);
    twos * threes
}

fn count_similar(input: &str, expected_count: i32) -> usize {
    return input
        .lines()
        .filter(|x| {
            let mut chars: HashMap<char, i32> = HashMap::new();
            x.chars().for_each(|c| *chars.entry(c).or_insert(0) += 1);
            for (_c, count) in chars {
                if count == expected_count {
                    return true;
                }
            }
            return false;
        })
        .count();
}

#[aoc(day2, part2)]
pub fn part2(input: &str) -> String {
    let mut lines: Vec<String> = input.lines().map(|x| x.to_string()).collect();

    lines.sort();

    for mut w in lines.windows(2){
        let diff = diff(&w[0], &w[1]);
        if diff.len() > 0 {
            return diff;
        }
    }
    unreachable!()
}

fn diff(a: &String, b: &String) -> String {
    let mut diff: i32 = 0;
    let mut sim: String = String::new();
    for (x,y) in a.chars().zip(b.chars()) {
        if x != y {
            diff+=1;
        } else {
            sim.push(x);
        }
    }
    if diff != 1 {
        return String::new();
    }
    return sim;
}
