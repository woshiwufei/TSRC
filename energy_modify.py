# -*- coding：utf-8 -*-
# """# -*- coding: utf-8 -*"""
from copy import deepcopy
import time

import networkx as nx
import random
import numpy as np
# import scipy
from queue import PriorityQueue

from compare_algorithm import main_func


def find_positive_seed(ds_: Dataset, negative_seed, num: int, negative_spread1: float) -> list:
    sss = time.time()
    positive_seeds_set = []
    G = deepcopy(ds_.G)
    aver_m = ds_.total_m / ds_.node_num
    temp_positive_set = []
    new_negative_spread = 0.0

    candidate_nodes = list(ds_.G.nodes - negative_seed)

    for node in candidate_nodes:
        if ds_.attr[node]['M'] <= aver_m:
            candidate_nodes.remove(node)
            G.remove_node(node)
    # 循环结束条件
    while len(positive_seeds_set) < num:
        q = PriorityQueue()
        for node in candidate_nodes:
            temp_positive_set = deepcopy(positive_seeds_set)
            temp_positive_set.append(node)

            jj = 0
            aver = 0.0
            while jj < ROUND:
                new_negative_spread, positive_marginal_increment, _ = run(ds_, G, negative_seed,
                                                                             temp_positive_set)
                aver += new_negative_spread / ROUND
                jj += 1
            q.put([aver - negative_spread1, node])
            new_negative_spread = aver
        max_node = q.get()
        positive_seeds_set.append(max_node[1])
        candidate_nodes.remove(max_node[1])
        negative_spread1 = new_negative_spread
    return positive_seeds_set


def runAlgorithm(ds, ns, p_num, negative_spread_):
    PS_list = [find_positive_seed(ds, ns, p_num, negative_spread_)]
    PS_list2 = main_func(ns, p_num)
