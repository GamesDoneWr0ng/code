import os
import neat
from datetime import datetime

class Nim():
    def __init__(self):    
        self.fyrstikker = 21
    
    def turn(self):
        trukket = input("Hvor mange fyrstikker vil du trekke? ")
        if trukket == "a":
            main.aiMode = 1
            return True
        elif trukket == "s":
            main.aiMode = 2
            return True
        elif trukket == "":
            return True
        else:
            trukket = int(trukket)
        if trukket > self.fyrstikker:
            print("Du kan ikke trekke flere fyrstikker en det er!")
            return True
        if trukket > 3:
            print("Du kan ikke trekke mere en 3 fyrstikker!")
            return True
        if trukket == 0:
            print("Du kan ikke trekke 0 fyrstikker!")
            return True
        self.fyrstikker -= trukket
        return False
    
    def aiTurn(self, trukket):
        self.fyrstikker -= trukket
        print("Ai-en trakk {} fyrstikker.".format(trukket))

class AI:
    def __init__(self):
        local_dir = os.path.dirname(__file__)
        config_path = os.path.join(local_dir, 'config-feedforward')
        self.config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

        self.pop = neat.Population(self.config)

        self.winner = self.pop.run(self.eval_genomes, 100)
    
    def eval_genome(self, genome, config):
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        main.player = 0
        fitness = 0
        
        nim.fyrstikker = 21
        while nim.fyrstikker > 0:
            input = format(nim.fyrstikker, "b")
            while len(input) < 5:
                input = "0"+input
            inputs = []
            
            for i in range(len(input)):
                inputs.append(input[i])
            for n, i in enumerate(inputs):
                i = int(i)
                inputs[n] = i
                    
            action = net.activate(inputs)
            
            trukket = 0
            for i in action:
                trukket = trukket + round(i)
            if trukket == 0:
                trukket = 1
            
            if trukket == main.perfectTrekk[str(nim.fyrstikker)]:
                fitness = fitness + 1
                
            nim.fyrstikker = nim.fyrstikker - trukket
            if nim.fyrstikker <= 0:
                if main.player == 0:
                    fitness = fitness + 1
                    
            main.player = (main.player+1)%2

        main.fitnesses.append(fitness)
        return fitness
    
    def eval_genomes(self, genomes, config):
        start=datetime.now()
        main.fitnesses = []
        for genome_id, genome in genomes:
            genome.fitness = self.eval_genome(genome, config)
        topFitness = 0
        for i in main.fitnesses:
            if i > topFitness:
                topFitness = i
        
        if topFitness > main.topFitness:
            main.topFitness = topFitness * 1
        
        print('"""  Generation {} """'.format(self.pop.generation))
        print('Time: {}'.format(datetime.now()-start))
        print('Average fitness: {}'.format(sum(main.fitnesses)/len(main.fitnesses)))
        print('Top fitness: {}'.format(topFitness))
        print('Top fitness alltime: {} \n'.format(main.topFitness))
    
    def playAI(self, config):
        net = neat.nn.FeedForwardNetwork.create(self.winner, config)
        input = format(nim.fyrstikker, "b")
        while len(input) < 5:
            input = "0"+input
        inputs = []
                
        for i in range(len(input)):
            inputs.append(input[i])
        for n, i in enumerate(inputs):
            i = int(i)
            inputs[n] = i
            
        action = net.activate(inputs)
        action = (round(abs(3*action[0]))%3+1)
        nim.aiTurn(action)
        

class Main():
    player = 0
    running = True
    aiMode = 0
    runs_per_net = 2
    fitnesses = []
    topFitness = 0
    perfectTrekk = {
                "21": 1,
                "20": 2,
                "19": 3,
                "18": 2,
                "17": 1,
                "16": 3,
                "15": 3,
                "14": 2,
                "13": 1,
                "12": 3,
                "11": 3,
                "10": 2,
                "9": 1,
                "8": 3,
                "7": 3,
                "6": 2,
                "5": 1,
                "4": 3,
                "3": 3,
                "2": 2,
                "1": 1
            }
    
    def tick(self):
        print("Det er {} fyrstikker.".format(nim.fyrstikker))
        if self.player == 0:
            self.player = 1
        else:
            
            if self.aiMode == 1:
                trekk = nim.fyrstikker % 4
                if trekk == 0:
                    trekk = 2
                nim.aiTurn(trekk)
                
                if nim.fyrstikker == 0:
                    print("The {} player is the winner!".format(self.player))
                    self.running = False
                    return
                
                self.player = 0
                return
            if self.aiMode == 2:
                ai.playAI(ai.config)
                
                if nim.fyrstikker == 0:
                    print("The {} player is the winner!".format(self.player))
                    self.running = False
                    return
                
                self.player = 0
                return
            self.player = 0
        while nim.turn():
            continue
        if nim.fyrstikker == 0:
            print("The {} player is the winner!".format((self.player+1)%2))
            self.running = False
            return

main = Main()
nim = Nim()
ai = AI()

nim.fyrstikker = 21
while main.running:
    main.tick()