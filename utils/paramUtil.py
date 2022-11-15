import numpy as np
ntu_action_labels = [6, 7, 8, 9, 22, 23, 24, 38, 80, 93, 99, 100, 102]

kinect_vibe_extract_joints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 21, 24, 38]


# Raw_offsets give the rough direction of each joint relative to root joint.
# For example, raw offset of root joint is [0,0,0]; raw offset of left hip is [-1, 0, 0].
# It could simply be [1, 0, 0] for all joint except root. However, this may affect the precision of transformation.
humanact12_raw_offsets = np.array([[0,0,0],
                               [1,0,0],
                               [-1,0,0],
                               [0,1,0],
                               [0,-1,0],
                               [0,-1,0],
                               [0,1,0],
                               [0,-1,0],
                               [0,-1,0],
                               [0,1,0],
                               [0,0,1],
                               [0,0,1],
                               [0,1,0],
                               [1,0,0],
                               [-1,0,0],
                               [0,0,1],
                               [0,-1,0],
                               [0,-1,0],
                               [0,-1,0],
                               [0,-1,0],
                               [0,-1,0],
                               [0,-1,0],
                               [0,-1,0],
                               [0,-1,0]])

vibe_raw_offsets = np.array([[0,0,0],
                               [0,-1,0],
                               [0,-1,0],
                               [-1,0,0],
                               [0,0,-1],
                               [0,-1,0],
                               [0,-1,0],
                               [0,0,-1],
                               [0,-1,0],
                               [0,1,0],
                               [0,1,0],
                               [0,1,0],
                               [0,1,0],
                               [0,1,0],
                               [0,1,0],
                               [0,1,0],
                               [0,1,0],
                               [0,-1,0]])

mocap_raw_offsets = np.array([[0, 0, 0],
                             [0, 1, 0],
                             [0, 1, 0],
                             [0, 1, 0],
                             [0, 1, 0],
                             [1, 0, 0],
                             [0, 1, 0],
                             [0, 1, 0],
                             [0, 1, 0],
                             [-1, 0, 0],
                             [-1, 0, 0],
                             [-1, 0, 0],
                             [0, -1, 0],
                             [0, -1, 0],
                             [0, -1, 0],
                             [0, -1, 0],
                             [0, -1, 0],
                             [0, -1, 0],
                             [0, -1, 0],
                             [0, -1, 0]])

# Define a kinematic tree for the skeletal struture
humanact12_kinematic_chain = [[0, 1, 4, 7, 10], [0, 2, 5, 8, 11], [0, 3, 6, 9, 12, 15], [9, 13, 16, 18, 20, 22], [9, 14, 17, 19, 21, 23]]

mocap_kinematic_chain = [[0, 1, 2, 3], [0, 12, 13, 14, 15], [0, 16, 17, 18, 19], [1, 4, 5, 6, 7], [1, 8, 9, 10, 11]]

vibe_kinematic_chain = [[0, 12, 13, 14, 15], [0, 9, 10, 11, 16], [0, 1, 8, 17], [1, 5, 6, 7], [1, 2, 3, 4]]

mocap_action_enumerator = {
    0: "Walk",
    1: "Wash",
    2: "Run",
    3: "Jump",
    4: "Animal Behavior",
    5: "Dance",
    6: "Step",
    7: "Climb"
}

humanact12_coarse_action_enumerator = {
    1: "warm_up",
    2: "walk",
    3: "run",
    4: "jump",
    5: "drink",
    6: "lift_dumbbell",
    7: "sit",
    8: "eat",
    9: "turn steering wheel",
    10: "phone",
    11: "boxing",
    12: "throw",
}

humanact12_fine_action_enumerator = {
    101: "warm_up_wristankle",
    102: "warm_up_pectoral",
    103: "warm_up_eblowback",
    104: "warm_up_bodylean_right_arm",
    105: "warm_up_bodylean_left_arm",
    106: "warm_up_bow_right",
    107: "warm_up_bow_left",
    201: "walk",
    301: "run",
    401: "jump_handsup",
    402: "jump_vertical",
    501: "drink_bottle_righthand",
    502: "drink_bottle_lefthand",
    503: "drink_cup_righthand",
    504: "drink_cup_lefthand",
    505: "drink_both_hands",
    601: "lift_dumbbell with _right hand",
    602: "lift_dumbbell with _left hand",
    603: "Lift dumbells with both hands",
    604: "lift_dumbbell over head",
    605: "lift_dumbells with both hands and bend legs",
    701: "sit",
    801: "eat_finger_right",
    802: "eat_pie or hamburger",
    803: "Eat with left hand",
    901: "Turn steering wheel",
    1001: "Take out phone, call and put phone back",
    1002: "Call with left hand",
    1101: "boxing_left_right",
    1102: "boxing_left_upwards",
    1103: "boxing_right_upwards",
    1104: "boxing_right_left",
    1201: "throw_right_hand",
    1202: "throw_both_hands",
}

# humanact12_action_enumerator = {
#     0: 'warm_up_wristankle',
#     1: 'warm_up_pectoral',
#     2: 'warm_up_eblowback',
#     3: 'walk',
#     4: 'run',
#     5: 'jump_handsup',
#     6: 'drink_bottle_righthand',
#     7: 'drink_bottle_lefthand',
#     8: 'lift_dumbles_right',
#     9: 'lift_dumbles_left',
    # 10: 'lift_dumbles_both',
    # 11: 'lift_dumbles_updown',
    # 12: 'warm_up_bodylean',
    # 13: 'warm_up_bow_right',
    # 14: 'warm_up_bow_left',
    # 15: 'jump_vertical',
    # 16: 'lift_dumbles_wholeupdown',
    # 17: 'sit',
    # 18: 'eat_finger_right',
    # 19: 'eat_pie',
    # 20: 'drive',
    # 21: 'phone_right',
    # 22: 'box_left_right',
    # 23: 'box_left',
    # 24: 'box_right',
    # 25: 'throw_right',
    # 26: 'drink_cup_righthand',
    # 27: 'drink_cup_righthand',
    # 28: 'eat_finger_left',
    # 29: 'phone_left',
    # 30: 'throw_both',
    #                   }
humanact12_action_enumerator = {
   0: "default",
   1: "주위를 둘러보며 리모컨 찾기",
   2: "혼자 스트레칭 하기",
   3: "상대방 발로 밀치기",
   4: "상대방에게 비키라고 손짓하기",
   5: "자리에서 비켜주기",
   6: "리모컨 들기",
   7: "소파에 앉기",
   8: "TV 전원 켜기",
   9: "옆 사람 어깨 밀치기",
   10: "리모컨으로 채널 조정",
   11: "혼자 발장구 치기",
   12: "TV 가리키면서 웃기",
   13: "스스로 얼굴 손으로 가리며 한숨 쉬기",
   14: "옆에 같이 주저 앉기",
   15: "자기 무릎에 고개를 파묻기",
   16: "상대방 어깨 토닥거림",
   17: "고개 들며 쳐다보기",
   18: "아니라며 고개 젓기",
   19: "앉은 상태에서 상대방 안아주기",
   20: "상대방 머리 쓰다듬기",
   21: "상대방 어깨 토닥거리며 고개 끄덕거리기",
   22: "상대방 손 잡기",
   23: "케이크 들고 나타나기",
   24: "생일 노래 부르면서 축하해주기",
   25: "깜짝 놀라기",
   26: "상대방 어깨 툭툭치기",
   27: "혼자 두 손 모으기 (소원 비는 자세 )",
   28: "생일 폭죽 터트리기",
   29: "케이크 자르기",
   30: "케이크 접시에 덜어주기",
   31: "선물 들고 오기",
   32: "상대방에게 선물 건네기",
   33: "문 열고 들어가기",
   34: "앉은 상태에서 상대방에게 가볍게 목례하기",
   35: "환자에게 의자에 앉으라고 손짓하기",
   36: "의자에 앉기",
   37: "환자를 향해 돌려 앉기",
   38: "의사에게 아픈 부위를 가리키며 증상 설명",
   39: "환자 아픈곳을 보며 진찰하기",
   40: "의자에서 일어나기",
   41: "문 열고 나가기",
   42: "주머니에서 핸드폰 꺼내기",
   43: "걸으면서 핸드폰 검색하기",
   44: "위쪽에 있는 출구 표지판 보며 두리번거리기",
   45: "역무원에게 다가가기",
   46:  "역무원에게 핸드폰 보여주며 질문하기",
   47: "보여준 핸드폰 자세히 들여다보기",
   48: "상대방을 보면서 손으로 경로 알려주기",
   49: "알려준 방향 쳐다보며 고개 끄덕이기",
   50: "손짓으로 방향 가리키며 역무원에게 다시 물어보기",
   51: "고개 끄덕거리기",
   52: "셀카로 사진 찍기",
   53: "행인에게 다가가서 핸드폰 건네기",
   54: "핸드폰 받기",
   55: "일행에게 사진 찍을 장소 가리키기",
   56: "포즈 취하기",
   57: "가까이 오라고 손짓 하기",
   58: "포즈 취하기",
   59: "사진 찍어주기",
   60: "다른 포즈 유도하기",
   61: "다시 포즈 취하기",
   62: "핸드폰 돌려주기",
   63: "핸드폰 받으면서 감사 인사 하기",
   64: "모여서 사진 확인하기",
   65: "상대방에게 핸드폰 보여주기",
   66: "컵 들고 마시는 제스처",
   67: "상대방 어깨 치면서 웃기",
   68: "기지개 펴기",
   69: "혼자 머리 정리하기",
   70: "혼자 팔짱끼고 다리 꼬기",
   71: "박수 치면서 웃기",
   72: "입 가리고 웃기",
   73: "행거에서 옷 고르기",
   74: "행거에서 상대방에게 어울리는 옷 추천해주기",
   75: "거울 앞에서 옷 대보기",
   76: "옷 2개 들어서 비교하기",
   77: "상대방이 2개 중에 옷 골라주기",
   78: "택에 적힌 옷 사이즈 확인하기",
   79: "옷 들고 가서 계산하기",
   80: "옷 개서 쇼핑백에 넣어주기",
   81: "쇼핑백 들기",
   82: "점원이 90도로 인사하기",
   83: "허리 숙여 인사하기",
   84: "상대방과 악수하기",
   85: "명함 건네주기",
   86: "받은 명함 보기",
   87: "상대방 쳐다보며 질문하기",
   88: "손짓하며 설명하기",
   89: "고개 끄덕거리며 상대방 쳐다보기",
   90: "종이 쳐다보기",
   91: "고개 갸우뚱하기",
   92: "종이 쳐다보며 고개 끄덕거리기",
   93: "팔짱 끼고 고개 갸우뚱하기",
   94: "손 들어서 의견 제시하기",
   95: "자리에서 일어나 악수하기",
   96: "걸으면서 메모 들여다보기",
   97: "장바구니를 들기",
   98: "채소 2개 들고 비교하기",
   99: "다른 채소 들어 보여주기",
   100: "채소 장바구니에 넣기",
   101: "두리번거리면서 물건 찾기",
   102: "장바구니를 들고 장소 가리키기",
   103: "높은 곳을 가리키기",
   104: "높은 곳에서 물건 꺼내기",
   105: "물건 받아서 장바구니에 담기",
   106: "마이크 두손으로 쥐기",
   107: "마이크 내리고 자료화면 바라보기",
   108: "자료화면 쪽으로 다가가기",
   109: "손으로 자료 화면 가리키기",
   110: "자료화면을 가리킨 손을 내리고 설명하면서 정면보기",
   111: "오른쪽으로 천천히 걸어가며 설명하기",
   112: "앞으로 돌아보며 뒤에 있는 자료화면 가리키기",
   113: "고개 끄덕이면서 자료화면을 가리킨 손 거두기",
   114: "왼쪽으로 천천히 걸어오기",
   115: "앞으로 한 발자국 나가서 90도 인사",
   116: "손으로 갯수를 세는 제스처",
   117: "손으로 자료화면 가리키기",
   118: "종이를 넘기는 제스처",
   119: "종이를 쳐다보다가 고개를 들면서",
   120: "팔짱을 끼면서",
   121: "두 손을 무릎 위에 올리면서",
   122: "두 손으로 허공에 원을 그리면서",
   123: "그린 원의 일부분을 표현하면서 (ex 더 작은 원을 그리며)",
   124: "왼손으로 뒤에 전시된 작품을 지칭하는 제스처",
   125: "손을 내리지말고 고개만 돌려 관객을 보면서 작품 설명",
   126: "손을 내리면서 마이크 쥔 손을 바꾸기",
   127: "큐카드를 넘기고 내용 확인",
   128: "큐카드를 내리고 정면 보면서 설명하기",
   129: "관객들에게 앞으로 한 발짝 다가가기",
   130: "멀리 있는 관객을 가리키는 제스처 (질문 받는 제스처)",
   131: "손을 거두면서 고개 끄덕이기",
   132: "관객 뒤쪽에 있는 작품을 가리키며",
   133: "관객 뒤쪽에 있는 작품 쪽으로 이동",
   134: "손을 흔들며 인사",
   135: "두 손으로 제품을 들어서 보여주면서",
   136: "손으로 시청자 카메라 를 가리키면서",
   137: "손뼉을 치면서",
   138: "손을 뻗어서 제품을 더 가까이 보여주면서",
   139: "두 손을 모으면서",
   140: "제품의 장점을 손으로 세면서 (첫번째, 두번째)",
   141: "손으로 최고 표시를 하면서",
   142: "앉은 상태로 마무리 인사",
}

ntu_action_enumerator = {
    1: "drink water",
    2: "eat meal or snack",
    3: "brushing teeth",
    4: "brushing hair",
    5: "drop",
    6: "pickup",
    7: "throw",
    8: "sitting down",
    9: "standing up (from sitting position)",
    10: "clapping",
    11: "reading",
    12: "writing",
    13: "tear up paper",
    14: "wear jacket",
    15: "take off jacket",
    16: "wear a shoe",
    17: "take off a shoe",
    18: "wear on glasses",
    19: "take off glasses",
    20: "put on a hat or cap",
    21: "take off a hat or cap",
    22: "cheer up",
    23: "hand waving",
    24: "kicking something",
    25: "reach into pocket",
    26: "hopping (one foot jumping)",
    27: "jump up",
    28: "make a phone call or answer phone",
    29: "playing with phone or tablet",
    30: "typing on a keyboard",
    31: "pointing to something with finger",
    32: "taking a selfie",
    33: "check time (from watch)",
    34: "rub two hands together",
    35: "nod head or bow",
    36: "shake head",
    37: "wipe face",
    38: "salute",
    39: "put the palms together",
    40: "cross hands in front (say stop)",
    41: "sneeze or cough",
    42: "staggering",
    43: "falling",
    44: "touch head (headache)",
    45: "touch chest (stomachache or heart pain)",
    46: "touch back (backache)",
    47: "touch neck (neckache)",
    48: "nausea or vomiting condition",
    49: "use a fan (with hand or paper) or feeling warm",
    50: "punching or slapping other person",
    51: "kicking other person",
    52: "pushing other person",
    53: "pat on back of other person",
    54: "point finger at the other person",
    55: "hugging other person",
    56: "giving something to other person",
    57: "touch other person's pocket",
    58: "handshaking",
    59: "walking towards each other",
    60: "walking apart from each other",
    61: "put on headphone",
    62: "take off headphone",
    63: "shoot at the basket",
    64: "bounce ball",
    65: "tennis bat swing",
    66: "juggling table tennis balls",
    67: "hush (quite)",
    68: "flick hair",
    69: "thumb up",
    70: "thumb down",
    71: "make ok sign",
    72: "make victory sign",
    73: "staple book",
    74: "counting money",
    75: "cutting nails",
    76: "cutting paper (using scissors)",
    77: "snapping fingers",
    78: "open bottle",
    79: "sniff (smell)",
    80: "squat down",
    81: "toss a coin",
    82: "fold paper",
    83: "ball up paper",
    84: "play magic cube",
    85: "apply cream on face",
    86: "apply cream on hand back",
    87: "put on bag",
    88: "take off bag",
    89: "put something into a bag",
    90: "take something out of a bag",
    91: "open a box",
    92: "move heavy objects",
    93: "shake fist",
    94: "throw up cap or hat",
    95: "hands up (both hands)",
    96: "cross arms",
    97: "arm circles",
    98: "arm swings",
    99: "running on the spot",
    100: "butt kicks (kick backward)",
    101: "cross toe touch",
    102: "side kick",
    103: "yawn",
    104: "stretch oneself",
    105: "blow nose",
    106: "hit other person with something",
    107: "wield knife towards other person",
    108: "knock over other person (hit with body)",
    109: "grab other person’s stuff",
    110: "shoot at other person with a gun",
    111: "step on foot",
    112: "high-five",
    113: "cheers and drink",
    114: "carry something with other person",
    115: "take a photo of other person",
    116: "follow other person",
    117: "whisper in other person’s ear",
    118: "exchange things with other person",
    119: "support somebody with hand",
    120: "finger-guessing game (playing rock-paper-scissors)",
     }

