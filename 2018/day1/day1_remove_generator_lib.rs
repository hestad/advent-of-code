use std::collections::HashSet;

#[aoc_generator(day1)]
pub fn input_generator(input: &str) -> Vec<i32> {
    input
        .lines()
        .map(|x| x.parse::<i32>().unwrap())
        .collect()
}

#[aoc(day1, part1)]
pub fn part1(input: &Vec<i32>) -> i32 {
    input.iter().sum()
}

#[aoc(day1, part2)]
pub fn part2(input: &Vec<i32>) -> i32 {
    let mut frequencies: HashSet<i32> = HashSet::new();
    let mut sum: i32 = 0;

    for (_i, item) in input.iter().enumerate().cycle() {
        sum += item;
        if frequencies.contains(&sum) {
            return sum;
        }
        frequencies.insert(sum);
    }
    unreachable!()
}