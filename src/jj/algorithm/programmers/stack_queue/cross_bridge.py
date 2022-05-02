# source: https://programmers.co.kr/learn/courses/30/lessons/42583

'''
트럭 여러 대가 일차선 다리를 정해진 순으로 건넌다.
모두 건너려면 최소 몇 초가 걸리는가.
다리에 최대 bridge_length 대 올라갈 수 있다.
다리는 weight 이하까지 견딜 수 있다. (단, 다리에 완전히 오르지 않은 트럭의 무게 무시)
'''

def solution(bridge_length, weight, truck_weights):
    # bridge_length: 트럭이 올라갈 수 있는 수
    # weight: 다리가 견디는 무게
    # truck_weights: 트럭 별 무게
    
    # 모든 트럭이 다리를 건너는데 최소 몇 초가 걸리는지 return.
    
    time = 0 # 걸린 시간
    trucks_on_bridge = [0] * bridge_length # 다리 위에 있는 트럭의 무게를 넣을 배열.
    weight_bridge_handling = 0 # 현재 다리가 견디고 있는 무게
    
    # 시간 효율성을 위해 truck_weights를 뒤집는다.
    # truck_weights.pop(0)는 첫 원소를 빼고 한 칸씩 앞으로 모두 땡기므로 O(n)
    # truck_weights.pop()은 O(1)
    truck_weights = truck_weights[::-1]
    
    while trucks_on_bridge:
        time += 1
        
        # 다리를 건넌 트럭의 무게를 빼준다.
        weight_bridge_handling -= trucks_on_bridge.pop()
        
        if truck_weights:   
            # 다리가 뒤 트럭이 더 들어와도 무게를 견딜 수 있다면,
            if truck_weights[-1] + weight_bridge_handling <= weight:
                # 
                weight_bridge_handling += truck_weights[-1]
                trucks_on_bridge.insert(0, truck_weights.pop())
            else:
                trucks_on_bridge.insert(0,0)
    
    return time