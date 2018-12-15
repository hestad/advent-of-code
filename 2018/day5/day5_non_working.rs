use std::str;

#[aoc_generator(day5)]
pub fn day5_generator(input: &str) -> Vec<u8> {
    return input.to_string().into_bytes();
}

#[aoc(day5, part1)]
pub fn part5(input: &Vec<u8>) -> String {
    let mut polymer:Vec<u8> = input.iter().map(|x| *x).collect();
    loop {
        for (i, _item) in polymer.clone().iter().enumerate() {
            if i > polymer.len()-2 {
                return (*str::from_utf8(&polymer).unwrap()).to_string();
            }
            if is_opposite(polymer[i], polymer[i+1]) {
                polymer.remove(i);
                polymer.remove(i);
                break;
            }
        }
    }
}

fn is_opposite(a: u8, b: u8) -> bool {
    if a > b {
        return b+32 == a;
    }
    return a+32 == b;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        assert_eq!(part5(&day5_generator("dabAcCaCBAcCcaDA")), "dabCBAcaDA");
    }
}