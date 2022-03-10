from fuzzingbook.MutationFuzzer import MutationFuzzer
from fuzzingbook.Coverage import Coverage
import matplotlib.pyplot as plt
import random
import string
from urllib.parse import urlparse
import validators
from IPy import IP


def delete_random_char(s):
    if s == '':
        return s
    pos = random.randint(0, len(s) - 1)
    return s[:pos] + s[pos+1:]


def add_random_char(s):
    pos = random.randint(0, len(s) - 1)
    random_character = chr(random.randrange(32, 127))
    return s[:pos] + random_character + s[pos:]


def flip_random_character(s):
    if s == '':
        return s
    pos = random.randint(0, len(s) - 1)
    c = s[pos]
    bit = 1 << random.randint(0, 6)
    new_c = chr(ord(c) ^ bit)
    return s[:pos] + new_c + s[pos + 1:]


def shuffle_chars(s):
    chars = list(s)
    shuffled = random.sample(chars, len(chars))
    outputString = ''
    outputString = outputString.join(shuffled)
    return outputString


def get_random_punctuation(s):
    length = len(s)
    listofpunctuation = string.punctuation
    result_str = ''.join(random.choice(listofpunctuation) for i in range(length))
    return result_str


def get_lines_covered(func, arg):
    with Coverage() as cov:
        func(arg)
    return len(cov.coverage()), cov.coverage()


def calculate_cumulative_coverage(population, func):
    cumulative_coverage = []
    all_coverage = set()

    for inp in population:
        with Coverage() as cov:
            func(inp)
        all_coverage |= cov.coverage()
        cumulative_coverage.append(len(all_coverage))
    return cumulative_coverage


def fuzzy_user(func, seed, label):
    trial = 2000
    cumulative_coverage = []
    mutators = [delete_random_char, add_random_char, flip_random_character, shuffle_chars, get_random_punctuation]
    seed_line_covered, covered_set = get_lines_covered(func, seed)
    population = [(seed, seed_line_covered)]

    for i in range(trial):
        seeds = [seed[0] for seed in population]
        lines_covered = [seed[1] for seed in population]
        seed_choice = random.choices(seeds, lines_covered)
        mutator = mutators[random.randint(0, 4)]
        mutated_seed = mutator(seed_choice[0])
        mutated_lines_covered, mutated_covered_set = get_lines_covered(func, mutated_seed)

        if len(covered_set | mutated_covered_set) > len(covered_set):
            covered_set |= mutated_covered_set
            population.append((mutated_seed, mutated_lines_covered))
            cumulative_coverage.append(len(covered_set))

    plt.plot(cumulative_coverage, label)


def fuzzy_built(func, seed, label):
    trials = 15
    fuzzer = MutationFuzzer([seed])

    population = []
    for i in range(0, trials):
        population.append(fuzzer.fuzz())

    cumulative_coverage = calculate_cumulative_coverage(population, func)
    plt.plot(cumulative_coverage, label)


def is_valid_url(url):
    try:
        supported_schemes = ["http", "https"]
        result = urlparse(url)
        if result.scheme not in supported_schemes:
            raise ValueError("Scheme must be one of " + repr(supported_schemes))
        if result.netloc == '':
            raise ValueError("Host must be non-empty")
    except ValueError:
        return False
    return True


def is_valid_email(email):
    try:
        validators.email(email)
    except ValueError:
        return False
    return True


def is_valid_ip(ip):
    try:
        IP(ip)
        return True
    except ValueError:
        return False


fuzzy_built(is_valid_url, "https://www.google.com/search?q=google&rlz=1C5CHFA_enCA758CA758&oq=google&aqs=chrome..69i57j69i60l3j69i65j69i60.4544j0j7&sourceid=chrome&ie=UTF-8", "r")
fuzzy_user(is_valid_email, "nishanpaul12011996se@gmail.com", "g")
fuzzy_user(is_valid_ip, "001.002.003.004.005.006", "b")

plt.show()