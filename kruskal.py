class Kraskal:
    def __init__(self, graph):
        self.FIRST = 0
        self.SECOND = 1
        self.WEIGHT = 2
        self.label = []
        self.weight = None
        self.edges = [[]]
        self.result = [[]]
        self.edges = graph
        self.init_label()

    def get_weight(self):
        return self.weight

    def init_label(self):
        for i in range(len(self.label)):
            self.label[i] = i

    def get_min_graph(self):
        self.do_sorting()
        self.weight = 0
        self.result[0] = self.edges[0]
        self.label[self.edges[0][self.SECOND]] = self.edges[0][self.FIRST]
        self.weight += self.edges[0][self.WEIGHT]

        i = 1
        for j in range(1, len(self.edges)):
            if self.label[self.edges[j][self.FIRST]] == self.label[self.edges[j][self.SECOND]]:
                continue
            
            value_to_change = self.label[self.edges[j][self.SECOND]]
            change_value = self.label[self.edges[j][self.FIRST]]

            for k in range(1, len(self.label)):
                if self.label[k] == value_to_change:
                    self.label[k] = change_value
            self.weight += self.edges[j][self.WEIGHT]
            i += 1
            self.result[i] = self.edges[j]

        return self.result

    def do_sorting(self):
        self.sort(0, len(self.edges) - 1)

    def sort(self, start, end):
        if start >= end:
            return
        
        i = start
        j = end
        cur = int((i - j) / 2)

        while i < j:
            while i < cur and self.edges[i][self.WEIGHT] <= self.edges[cur][self.WEIGHT]:
                i += 1
            while j > cur and self.edges[j][self.WEIGHT] >= self.edges[cur][self.WEIGHT]:
                j -= 1
            
            if i < j:
                i, j = j, i
                if i == cur:
                    cur = j
                elif j == cur:
                    cur = i
        
        self.sort(start, cur)
        self.sort(cur + 1, end)


if __name__ == '__main__':
    g = [[0, 1, 6],
             [0, 2, 10],
             [1, 3, 4],
             [1, 4, 2],
             [3, 4, 3],
             [2, 3, 2],
             [2, 6, 4],
             [2, 5, 3],
             [6, 5, 4],
             [3, 5, 2],
             [3, 7, 4],
             [5, 7, 2],
             [5, 8, 3],
             [8, 7, 1],
             [2, 7, 1]]

    krask = Kraskal(g)
    result = krask.get_min_graph()
    for arr in result:
        if arr[krask.WEIGHT] != 0:
            print(arr)
    print(krask.get_weight())
