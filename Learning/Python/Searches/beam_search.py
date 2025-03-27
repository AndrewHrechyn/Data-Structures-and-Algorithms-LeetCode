from numpy import array

def beam_search(distances, beta):
    paths_so_far = [[list(), 0]]

    for idx, tier in enumerate(distances):
        if idx > 0:
            print(f'Paths kept after tier {idx - 1}:')
            print(*paths_so_far, sep='\n')
        paths_at_tier = list()

        for i in range(len(paths_so_far)):
            path, distance = paths_so_far[i]

            for j in range(len(tier)):
                path_extended = [path + [j], distance + tier[j]]
                paths_at_tier.append(path_extended)

        paths_ordered = sorted(paths_at_tier, key=lambda element: element[1])

        paths_so_far = paths_ordered[:beta]
        print(f'\nPaths reduced to after tier {idx}: ')
        print(*paths_ordered[beta:], sep='\n')

    return paths_so_far


if __name__ == '__main__':

    dists = [[1, 4, 6, 8],
             [5, 2, 3, 4]]
    dists = array(dists)

    best_paths = beam_search(dists, 2)
    print('\nThe best paths:')
    for beta_path in best_paths:
        print(beta_path)