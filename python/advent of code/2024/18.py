import re
data = """
29,13
13,16
8,5
1,25
33,55
69,64
69,57
15,16
20,31
39,29
23,29
40,13
31,16
18,13
2,1
10,3
19,30
57,45
34,17
33,19
20,13
65,45
22,7
33,63
49,69
27,23
41,63
1,17
33,8
7,25
65,64
39,58
47,67
23,19
17,28
57,43
27,1
17,3
58,65
21,25
3,17
33,25
33,24
18,27
14,5
29,5
35,68
3,24
18,11
39,25
67,58
2,27
21,13
32,11
59,65
37,21
64,67
16,15
15,0
11,11
54,61
63,58
61,51
33,51
3,25
37,51
31,21
49,54
7,2
56,63
65,67
67,63
14,19
20,25
2,9
37,62
37,6
63,49
17,5
54,63
53,67
39,15
49,57
37,26
53,59
43,3
17,6
30,7
65,65
35,55
42,59
15,7
29,49
40,55
25,22
33,18
60,59
19,25
41,4
43,15
59,63
29,17
35,11
39,20
55,41
63,65
56,67
57,41
31,19
69,54
23,11
41,14
13,2
35,27
23,7
38,19
59,55
63,51
59,38
53,52
9,23
47,66
43,57
31,59
39,59
48,65
38,29
23,9
2,17
2,23
62,69
36,11
34,45
13,20
31,25
37,3
65,61
27,29
8,3
11,37
66,69
69,63
7,27
65,53
27,15
3,13
56,45
21,35
55,50
53,57
14,27
55,60
12,3
32,59
15,15
33,57
49,61
19,8
29,55
32,23
55,35
14,35
14,13
61,47
11,7
35,61
53,41
0,7
5,20
46,63
7,11
37,23
1,3
37,29
37,57
12,9
26,21
29,4
25,19
4,13
65,57
55,65
67,67
48,63
47,58
29,23
53,63
7,14
57,56
41,68
27,24
3,27
1,19
52,67
69,66
56,41
63,53
13,22
33,52
9,17
3,31
64,57
11,20
13,15
27,4
39,65
35,60
61,70
3,1
43,43
45,69
9,19
65,62
67,56
8,13
11,15
41,60
62,61
51,61
36,21
21,6
19,13
42,11
37,22
69,67
57,51
33,46
36,9
9,12
21,23
57,52
20,23
11,23
9,7
25,13
33,56
32,55
59,64
51,63
56,49
10,1
5,30
59,60
35,56
39,60
27,16
40,19
43,12
23,13
38,69
0,21
36,29
63,46
29,33
22,1
16,21
57,40
35,29
4,7
30,21
38,59
59,51
55,49
25,10
10,15
5,5
3,21
57,63
31,57
66,59
43,64
19,19
33,17
1,23
55,67
35,53
22,13
17,4
68,53
33,23
37,25
31,33
24,29
26,1
11,3
15,21
57,61
37,17
61,69
25,5
41,61
29,59
29,28
6,13
19,27
50,57
7,21
51,47
66,57
46,65
0,31
43,69
29,16
61,56
31,3
29,2
3,7
63,55
37,15
39,9
23,12
11,10
53,45
35,2
13,4
68,59
21,2
16,29
21,5
63,69
39,19
51,65
30,23
12,25
47,59
53,51
43,55
17,27
53,58
25,7
21,27
32,63
1,43
9,5
69,65
37,1
8,23
5,17
54,43
61,55
53,46
33,20
51,62
7,7
29,11
28,21
13,10
47,65
53,69
57,53
33,53
33,15
49,65
3,15
5,22
39,11
8,7
59,67
19,17
8,33
49,59
25,9
33,29
29,1
57,67
24,23
19,16
53,66
5,21
25,20
66,47
43,56
43,65
67,55
9,11
60,41
7,17
1,26
47,44
51,67
20,33
61,65
5,25
63,54
39,28
57,65
49,55
34,51
23,26
46,69
35,1
42,55
19,5
33,47
69,59
31,0
7,32
36,69
10,21
41,11
23,6
69,69
47,51
54,69
35,7
39,70
36,65
35,10
37,49
33,2
26,5
68,51
3,30
7,13
53,65
53,68
31,13
63,59
67,54
48,61
1,12
37,27
30,11
15,14
1,15
41,64
1,11
47,63
19,11
5,11
61,49
19,15
21,22
16,23
69,55
21,3
41,57
5,29
21,9
5,9
0,15
34,27
4,17
13,21
29,0
65,66
15,25
31,9
50,53
32,27
9,15
1,27
13,9
43,17
11,42
24,15
41,7
30,49
70,51
51,50
36,27
52,39
31,22
27,21
60,63
53,47
27,14
67,57
33,9
55,63
15,17
4,19
28,9
9,20
33,7
55,43
55,64
24,3
25,17
6,5
24,17
33,59
9,18
35,58
43,50
18,7
63,61
37,52
55,54
55,58
67,59
25,6
59,61
23,20
55,66
15,1
7,29
4,27
60,55
5,12
59,62
12,17
28,29
40,25
26,9
5,8
14,23
39,63
49,51
17,25
25,26
29,20
66,51
3,9
60,39
39,2
42,61
41,15
35,66
55,51
25,23
15,3
12,23
9,26
28,13
59,66
69,61
37,63
11,5
18,1
41,19
53,50
65,59
31,12
51,69
40,67
26,29
55,57
21,7
5,24
23,31
3,18
25,18
7,1
42,51
35,25
6,15
3,23
19,2
9,0
39,17
21,17
7,10
22,19
36,59
49,63
15,26
51,55
25,28
23,17
41,55
7,9
29,7
37,54
16,27
30,53
35,54
53,48
13,17
59,58
13,19
69,62
2,21
57,46
39,54
58,61
26,13
3,6
42,69
58,39
20,27
11,12
65,55
19,14
34,15
40,65
47,69
57,69
45,67
38,67
19,20
4,33
4,15
27,5
47,52
45,61
30,47
21,10
63,68
59,57
7,16
69,48
11,25
31,17
33,60
29,6
3,32
17,13
26,25
55,56
30,9
55,55
17,17
35,59
29,15
67,51
59,59
61,67
69,53
29,18
28,25
12,13
16,5
34,11
11,6
55,52
65,40
32,45
39,69
27,9
28,27
58,69
30,57
11,31
34,25
59,53
63,52
41,65
33,1
70,57
59,69
8,21
5,7
1,13
52,59
11,27
5,15
7,5
61,57
23,16
23,21
57,49
11,9
65,51
33,3
17,15
37,61
45,65
39,7
5,23
48,69
11,18
57,44
43,51
67,65
39,23
59,42
50,69
9,3
55,59
65,63
7,33
34,65
39,6
1,8
26,19
38,65
53,61
29,57
31,55
31,15
57,58
55,53
27,17
17,7
11,29
63,64
29,53
42,53
7,31
32,31
10,25
54,41
11,21
49,43
9,34
63,62
57,48
53,55
19,9
38,55
35,19
47,57
63,57
17,23
20,19
5,1
53,49
35,69
5,31
8,37
55,69
33,13
37,53
19,18
53,9
67,53
51,42
35,67
65,69
1,31
10,23
31,23
30,17
29,58
29,10
15,19
67,47
19,21
9,9
37,47
11,17
34,63
60,67
35,6
13,25
36,51
31,7
33,54
15,2
27,6
34,1
45,60
57,50
25,1
5,19
17,16
51,3
34,29
19,7
69,68
18,25
9,25
24,1
24,13
37,65
35,13
1,20
37,56
11,13
31,11
23,27
7,26
25,21
40,57
57,57
52,65
17,19
53,56
45,18
27,34
50,65
6,1
34,7
13,7
61,63
45,63
36,49
43,14
4,1
64,51
13,5
44,67
31,2
63,60
20,9
0,25
14,7
43,68
35,21
55,42
57,55
27,3
67,64
53,44
61,59
6,19
67,49
37,24
2,3
59,41
36,13
51,60
64,55
33,11
21,21
50,59
15,23
52,55
9,13
5,13
55,47
3,10
36,63
43,67
23,15
20,5
9,1
29,54
43,62
13,13
15,27
21,16
8,17
21,28
43,11
63,63
23,23
30,25
52,63
21,40
5,4
44,63
33,4
35,49
37,69
35,51
35,63
63,66
32,7
31,1
23,8
31,27
23,1
23,5
59,68
35,65
10,41
37,19
43,66
23,24
39,24
56,69
50,63
34,13
40,11
39,61
15,11
6,7
25,27
33,27
55,45
33,45
5,2
17,24
39,16
62,53
35,17
15,18
33,58
33,5
27,13
11,14
62,65
44,57
13,33
32,19
16,1
39,62
43,47
34,21
35,15
66,53
25,15
19,3
40,63
49,67
36,19
33,66
11,19
41,21
67,69
32,15
60,53
29,19
15,12
36,15
25,8
7,37
37,8
10,5
43,53
19,23
11,8
35,22
7,35
35,57
57,39
8,25
17,21
21,18
25,25
45,51
23,25
21,15
7,23
7,30
3,11
1,29
1,4
19,4
4,25
33,21
18,23
58,53
30,45
27,2
9,21
43,58
15,10
1,5
42,29
43,63
69,51
54,47
47,68
39,13
37,7
53,53
33,69
27,19
22,25
36,17
59,32
28,57
5,3
32,49
33,67
1,33
53,54
1,1
57,47
18,19
27,12
23,10
57,59
29,3
17,1
11,1
38,17
19,43
45,21
41,69
22,29
39,53
37,59
69,60
2,15
41,59
23,4
10,29
51,45
39,67
8,9
50,67
2,29
61,53
21,45
67,45
49,60
47,48
15,29
31,26
47,56
33,49
2,13
47,61
27,11
25,11
6,23
3,19
35,23
11,32
39,57
15,5
1,7
7,19
6,27
68,69
61,61
17,11
29,25
56,61
21,11
37,67
38,11
3,3
14,25
15,8
40,15
5,10
62,57
31,14
45,57
13,1
31,5
25,3
37,11
1,35
10,9
5,28
7,15
58,55
35,9
5,55
21,43
66,31
28,37
50,11
17,39
69,25
47,41
45,37
15,52
15,35
7,53
65,14
17,63
13,31
15,63
45,13
3,48
44,43
55,3
15,9
45,25
47,29
5,53
39,46
47,12
39,45
46,51
63,32
49,15
16,63
11,55
15,69
10,35
56,27
70,33
15,59
62,39
32,35
53,23
51,7
47,45
63,7
27,25
56,29
51,14
26,59
56,3
43,26
49,7
17,45
29,47
60,47
53,4
0,53
9,41
57,9
10,57
47,13
37,38
41,23
39,43
22,31
23,52
49,30
45,5
3,4
61,12
61,4
2,53
58,25
21,44
17,55
17,54
28,41
67,23
26,67
45,29
3,47
66,17
34,37
46,33
27,52
69,18
4,37
13,37
27,53
5,59
47,35
49,8
37,31
64,35
45,52
7,68
64,9
35,37
63,2
58,19
47,5
27,59
49,34
53,12
3,43
45,10
13,38
25,31
41,8
41,44
67,32
20,11
17,46
59,7
12,67
7,43
27,32
50,27
51,41
15,56
24,31
5,68
25,53
53,11
63,23
55,23
18,67
41,31
19,38
47,27
25,48
67,19
2,47
17,70
1,51
9,60
59,16
25,51
29,9
60,13
61,6
15,44
35,31
68,1
31,70
53,21
21,64
3,40
59,5
5,56
7,67
59,22
55,5
8,29
5,48
55,0
61,34
19,52
55,6
21,31
63,31
15,47
43,37
17,42
3,57
69,9
11,50
19,57
33,39
37,44
5,45
25,33
63,47
3,65
1,32
28,61
54,1
69,21
41,47
23,53
38,33
58,15
33,36
46,3
48,5
43,45
65,31
10,63
55,19
67,42
39,51
9,35
11,45
25,57
7,61
29,42
13,47
21,19
51,37
16,57
21,29
64,47
17,37
27,35
32,5
34,49
56,33
59,23
22,39
49,18
27,47
4,55
3,44
13,48
21,65
43,31
50,25
13,57
25,49
39,49
11,39
69,7
45,23
21,70
51,13
57,23
1,41
15,31
6,47
15,30
54,11
28,65
66,27
15,20
69,37
50,5
19,53
21,48
31,51
9,63
61,13
56,13
40,31
21,67
67,5
19,61
64,23
41,5
51,5
7,69
45,54
58,23
54,3
49,5
61,41
19,62
55,39
55,10
5,63
51,15
25,43
1,56
45,49
22,43
51,39
2,63
22,61
33,43
57,12
70,13
29,61
17,49
27,41
39,36
50,43
45,9
31,41
3,29
37,13
21,39
68,39
31,49
27,51
55,13
69,29
35,4
68,17
1,67
31,29
69,20
44,27
23,63
60,51
41,17
61,33
69,26
67,25
66,5
27,57
6,35
69,35
23,40
51,22
51,16
44,31
7,51
1,49
13,65
46,43
1,58
53,35
47,14
58,5
64,11
45,36
11,36
41,2
26,47
13,45
9,31
25,29
50,45
21,1
15,55
51,20
65,39
59,26
19,59
35,43
64,37
9,33
61,1
9,65
7,54
27,44
9,43
55,37
56,21
25,50
57,10
42,47
19,35
31,37
45,15
58,7
25,61
37,36
61,10
49,32
63,0
61,31
15,41
37,2
24,45
8,47
45,39
55,27
17,61
45,17
67,37
36,37
27,54
7,47
51,27
0,67
29,60
51,49
53,26
5,37
47,9
21,61
7,50
63,19
45,33
54,37
19,39
49,21
7,57
57,17
1,9
11,53
23,51
43,29
67,20
45,1
23,34
40,51
47,34
11,28
59,9
28,45
53,17
13,69
15,68
69,5
67,35
30,65
5,33
48,31
17,47
4,51
49,23
57,11
57,19
57,24
39,38
17,31
16,67
37,32
18,57
9,45
55,38
68,11
2,41
19,31
58,45
14,39
46,9
17,41
52,21
49,27
46,47
3,59
7,66
65,5
25,39
41,33
28,51
63,45
51,1
50,3
69,11
11,47
1,34
17,44
21,41
23,66
60,25
55,61
2,35
65,4
31,61
48,39
67,39
16,9
18,69
58,29
41,39
64,3
53,31
49,11
45,45
25,38
59,29
17,57
55,15
13,40
17,60
33,41
59,45
43,38
3,67
69,3
11,57
23,59
4,57
15,45
63,17
5,39
41,1
7,55
65,30
8,39
45,46
15,60
26,69
67,1
65,25
13,44
6,61
39,40
5,43
46,21
61,29
45,7
33,62
69,31
19,60
11,51
31,53
62,43
19,51
33,35
57,2
1,21
7,41
32,69
33,33
41,45
63,16
29,31
17,34
14,53
48,57
45,11
45,35
63,67
49,1
65,37
27,27
51,57
35,36
21,59
49,29
20,47
7,49
49,47
60,19
23,68
29,63
27,39
69,39
45,27
63,30
53,1
12,61
3,69
29,27
25,36
9,55
0,49
43,5
12,57
63,34
14,41
19,47
43,7
47,21
70,31
64,49
29,41
13,3
60,7
61,14
39,55
21,63
51,29
3,55
41,49
15,13
61,19
59,47
19,66
44,13
59,17
39,21
51,48
45,19
47,25
5,42
59,37
21,36
51,9
29,39
23,55
59,11
51,19
48,45
19,49
53,37
62,37
40,45
21,50
9,58
19,54
23,49
15,54
36,47
1,47
31,28
15,32
29,69
44,39
67,43
10,67
43,35
57,7
13,11
65,19
3,45
6,39
67,41
5,47
6,41
56,25
23,67
19,36
18,55
49,49
47,7
39,33
55,21
57,25
69,14
59,15
11,33
35,41
9,39
11,48
1,63
61,25
61,23
25,67
67,29
59,25
9,68
49,17
61,35
35,44
21,69
1,44
9,38
45,53
4,47
9,32
47,1
66,45
23,37
46,31
48,23
52,1
28,33
65,43
27,55
5,41
9,37
63,3
27,56
61,39
60,35
61,45
5,61
64,21
44,3
53,25
8,41
35,35
10,39
26,57
55,28
48,15
3,38
34,41
39,27
49,50
19,64
26,43
7,63
41,41
19,55
6,59
62,31
65,49
66,37
7,45
65,27
25,37
67,9
41,42
12,45
13,61
16,37
53,19
63,21
21,51
3,66
69,45
67,13
60,9
57,38
13,29
19,1
36,33
68,5
49,35
21,53
30,37
11,60
55,1
63,29
21,56
13,35
32,41
27,37
23,3
24,63
29,29
46,29
8,45
47,43
12,55
63,9
44,17
65,21
43,1
47,37
43,27
67,66
9,52
29,37
55,31
40,37
40,49
2,37
2,51
12,51
47,10
47,17
65,22
53,18
19,40
8,51
63,11
59,50
66,15
49,3
7,36
11,66
27,63
62,23
61,21
52,11
47,36
47,3
68,37
9,54
11,63
11,70
2,69
18,31
69,49
61,17
13,51
1,42
69,46
35,34
25,34
43,41
19,46
59,1
43,44
11,41
3,53
47,49
38,43
55,17
11,59
47,28
1,60
17,43
19,41
65,15
66,35
5,67
46,7
12,65
67,15
10,47
31,64
49,56
55,29
42,33
65,42
53,43
6,63
7,64
35,33
41,37
23,50
33,32
13,58
53,15
2,61
5,49
31,40
66,11
60,31
39,48
48,19
62,41
41,35
47,19
1,65
9,29
13,34
56,7
9,51
59,43
1,69
15,50
4,35
54,29
5,60
63,26
17,51
44,7
60,43
0,39
25,35
51,21
6,45
61,2
63,33
9,49
7,52
31,39
13,68
45,6
41,34
37,41
5,27
69,17
29,67
28,31
27,7
19,42
31,65
29,21
13,62
2,55
39,47
66,1
4,59
44,41
67,24
41,18
45,26
60,3
19,67
45,43
15,67
15,61
1,45
41,43
51,51
23,60
51,38
47,11
37,37
13,46
51,17
31,47
43,48
28,67
61,5
47,39
25,68
7,65
52,17
55,25
1,57
31,30
25,44
21,42
68,43
46,59
35,3
38,41
57,35
13,56
25,55
58,33
43,61
62,13
67,7
65,28
55,22
27,45
37,35
3,33
55,33
16,39
63,35
51,11
59,27
4,63
13,67
35,40
51,33
54,21
19,50
45,0
26,61
69,1
43,39
62,49
70,25
19,37
56,15
69,47
69,23
48,7
25,45
32,67
1,53
42,5
17,29
16,65
59,31
5,51
7,59
4,69
49,39
65,23
53,5
39,52
68,45
21,33
31,63
27,43
10,45
17,67
41,0
14,65
54,17
21,37
3,41
15,49
19,34
30,63
61,43
39,35
53,7
54,9
23,43
41,25
43,25
57,5
64,27
53,14
11,61
5,54
51,31
51,6
62,17
33,38
49,33
63,13
55,7
52,27
65,24
65,11
57,18
25,41
27,33
69,42
43,24
23,69
67,26
21,62
61,20
39,8
24,59
13,64
29,65
43,21
47,33
2,67
19,33
39,41
37,55
38,1
51,8
44,29
65,47
69,13
65,41
39,31
6,33
24,37
53,40
14,49
28,49
63,6
57,33
41,40
11,43
41,67
53,32
59,19
44,47
68,7
39,1
61,11
48,41
12,53
45,47
31,69
61,24
1,39
45,41
67,2
62,45
5,65
53,33
62,9
70,39
17,65
62,21
69,8
40,5
12,41
45,24
14,69
24,41
46,41
25,54
15,39
12,29
50,37
66,7
60,29
31,38
63,27
52,35
69,15
36,41
19,45
13,32
24,33
11,65
65,34
41,13
5,69
23,35
66,9
29,45
47,55
65,1
9,47
32,33
30,35
63,41
40,21
8,61
21,52
59,33
37,33
17,33
41,3
42,17
4,65
17,53
57,21
59,13
16,47
67,11
54,33
19,58
23,39
63,43
29,43
21,47
13,23
68,33
61,37
41,51
58,35
33,65
43,49
11,35
67,3
35,39
67,22
42,19
30,43
65,17
30,61
30,67
51,25
54,7
31,35
65,12
53,24
21,57
55,16
27,67
17,69
35,5
33,31
23,46
57,31
49,31
23,47
11,69
51,59
46,17
35,30
67,40
42,37
23,41
39,30
31,45
46,55
4,39
9,57
29,35
15,51
31,52
22,47
22,59
25,47
69,33
21,58
38,13
67,33
33,61
44,53
42,41
51,53
64,13
27,49
59,3
57,4
51,24
62,5
55,9
46,39
51,52
63,25
25,59
19,29
47,53
53,3
17,40
58,31
41,10
22,53
13,27
37,5
41,29
69,41
5,52
57,36
39,3
42,7
47,24
69,22
45,31
9,27
18,63
65,33
67,17
49,41
57,15
15,46
49,2
48,37
55,20
3,63
39,26
42,27
13,36
37,42
33,37
22,33
49,9
59,21
5,35
67,18
47,47
13,39
21,66
23,61
27,61
54,25
51,40
47,31
43,30
57,29
49,13
10,43
1,61
61,27
15,43
23,33
46,15
3,37
65,13
49,19
14,61
15,53
61,9
53,13
5,57
51,36
25,56
52,29
31,43
15,37
38,49
1,55
65,44
59,35
3,51
29,51
51,43
47,4
48,11
47,42
3,50
37,43
11,67
3,49
26,41
61,50
65,3
13,63
65,29
15,57
31,50
65,20
17,48
37,4
45,55
67,21
59,39
37,39
41,53
39,22
10,53
60,17
25,62
28,47
13,49
21,49
57,3
19,65
55,36
30,39
67,62
61,3
27,69
9,69
59,48
22,55
9,67
69,43
68,29
8,69
31,67
41,9
61,36
43,32
63,39
57,8
45,59
67,68
19,63
11,49
9,64
51,23
26,49
52,31
51,34
67,61
67,4
17,32
7,3
58,11
13,55
13,53
49,48
70,3
63,5
49,53
68,49
15,33
51,46
24,65
3,35
53,39
56,19
57,13
45,3
28,69
15,65
16,59
65,7
69,19
43,59
16,35
65,38
64,17
28,63
12,33
3,5
49,28
49,14
67,27
55,11
45,22
47,38
35,45
43,22
23,45
24,53
35,32
68,13
37,45
56,31
50,31
48,49
23,57
43,13
5,66
43,4
9,59
9,61
64,43
25,63
45,20
43,23
39,39
52,5
64,7
17,9
9,53
31,31
63,18
61,28
26,65
42,35
7,58
63,1
49,16
65,9
49,45
4,43
30,33
27,38
21,55
13,43
13,30
68,35
55,34
24,57
45,50
1,37
49,20
47,15
27,40
32,43
18,49
3,46
20,55
67,28
58,1
67,31
17,59
13,41
63,37
49,25
63,15
44,9
41,27
49,37
48,1
49,22
62,27
35,47
25,69
52,3
21,68
9,62
27,36
61,7
7,39
57,37
66,49
44,35
38,47
43,9
22,37
69,10
51,10
39,37
7,44
1,59
53,29
43,33
47,23
39,5
1,64
37,9
60,45
3,61
55,14
59,49
57,27
17,35
23,65
53,27
19,69
44,1
10,49
27,31
65,35
1,62
47,26
42,23
61,15
7,56
43,19
13,59
39,34
27,65
35,46
25,65
43,16
57,1
16,51
23,64
3,39
18,37
69,27
51,35
19,44
37,30
29,66
32,17
9,46
33,28
26,26
39,66
68,32
43,46
26,7
8,22
36,61
46,11
62,30
4,28
20,61
66,32
16,46
18,68
56,26
37,10
24,35
22,23
69,6
30,20
3,36
2,49
35,16
42,54
18,66
10,17
56,1
62,42
5,50
12,43
14,45
16,55
26,53
65,8
20,41
39,44
6,70
70,35
17,50
14,67
1,22
14,24
20,37
42,52
42,0
30,69
6,58
52,28
4,62
20,54
39,50
10,0
64,60
8,26
21,54
20,64
20,18
34,53
31,62
6,8
27,20
8,53
36,60
8,56
48,2
8,62
1,28
10,65
16,69
34,23
6,48
62,24
24,56
41,56
24,52
46,46
38,56
62,6
0,24
20,36
10,54
45,62
48,12
34,43
30,3
44,46
65,0
40,40
50,52
4,29
64,69
68,9
29,44
24,32
6,38
42,68
34,14
40,26
50,58
50,38
59,40
8,57
34,44
44,50
21,60
38,31
64,1
66,14
8,28
55,24
2,26
2,46
48,46
34,60
50,56
9,28
32,22
60,10
30,70
34,32
50,50
19,48
68,64
18,59
68,30
69,28
66,4
9,44
20,63
10,20
64,25
50,51
48,0
6,29
7,12
52,2
38,2
49,26
24,40
13,42
2,25
40,46
46,61
47,60
68,61
9,14
24,64
14,14
24,24
6,18
60,12
68,16
6,44
51,44
2,54
37,46
8,32
52,8
40,14
10,50
23,54
60,22
12,21
24,49
50,1
69,4
33,44
35,48
62,3
22,28
9,42
32,18
41,70
2,6
28,68
69,24
34,56
32,4
24,50
12,48
49,68
38,12
2,62
0,18
14,22
24,47
64,62
47,40
13,66
28,46
14,16
54,19
31,56
28,26
34,54
39,12
26,37
16,38
24,68
42,57
46,54
68,4
34,61
56,20
14,6
9,8
38,16
32,62
20,40
34,35
0,48
58,37
42,24
21,38
61,8
32,48
50,39
35,14
7,42
28,23
34,36
62,16
10,26
38,15
20,43
38,3
12,30
14,20
32,54
36,62
62,22
54,10
32,68
50,19
24,70
44,25
16,28
38,39
68,62
4,34
26,54
2,42
62,29
12,46
56,10
48,14
63,24
22,44
54,8
58,24
42,56
6,60
10,69
22,32
44,20
56,22
68,19
2,52
20,15
35,64
52,30
36,46
17,10
32,58
16,60
0,30
15,24
38,20
18,35
2,36
29,48
4,12
26,52
31,68
43,34
16,62
34,39
36,68
68,8
41,20
37,40
65,26
49,62
66,66
42,12
35,20
38,27
18,61
8,31
25,58
58,16
30,44
66,28
43,60
52,10
4,31
58,26
26,62
50,16
11,58
0,54
20,58
0,29
24,43
30,2
64,18
28,43
25,40
62,4
6,65
56,51
18,0
12,58
64,63
33,6
1,52
18,34
40,66
44,62
70,30
0,23
35,38
23,36
31,18
68,21
0,44
6,51
9,24
28,52
70,41
22,66
13,50
66,0
8,52
10,31
10,22
67,70
6,32
69,70
24,60
4,70
22,40
36,40
24,42
31,24
16,22
18,33
42,66
40,42
42,64
44,55
14,56
46,58
58,10
24,39
8,20
16,10
32,60
17,0
2,50
6,68
36,34
12,70
1,30
31,60
26,66
60,20
14,57
56,30
26,23
4,20
4,61
10,12
20,53
16,70
22,27
22,5
30,34
52,20
4,38
10,19
42,2
68,22
46,48
2,34
22,70
12,39
34,34
14,29
55,32
8,11
14,40
70,10
68,70
37,60
10,60
10,34
34,4
10,28
38,18
64,65
20,51
0,51
64,8
32,46
18,70
41,48
29,56
70,14
63,4
16,32
44,24
50,13
37,50
33,26
62,28
36,66
42,48
24,30
5,34
24,27
38,58
64,70
38,62
24,55
2,10
62,20
44,56
7,34
0,11
54,28
53,0
8,12
60,37
28,32
13,26
34,52
45,16
36,43
42,44
25,46
8,68
46,35
18,60
20,34
55,2
15,64
60,33
4,45
52,58
58,2
10,58
19,12
6,31
60,49
50,2
45,8
15,70
26,20
70,55
60,21
30,60
38,28
32,53
34,58
26,51
20,50
66,56
52,13
8,1
38,48
6,11
56,14
55,68
24,20
63,8
44,28
46,40
54,26
68,67
5,44
21,30
24,61
14,4
6,24
44,65
32,42
70,43
4,4
59,52
11,54
64,6
12,49
20,35
65,50
2,48
44,66
46,45
70,11
27,8
3,34
24,8
29,46
48,36
12,8
50,26
50,42
4,58
10,11
9,70
57,66
8,44
28,53
58,60
48,62
14,0
37,18
1,46
8,48
11,62
44,0
27,62
39,0
68,44
58,8
10,62
31,20
28,35
8,36
0,66
34,22
42,40
26,45
10,64
49,42
70,4
10,55
52,47
10,40
59,14
66,61
56,55
36,22
50,12
24,21
70,62
38,0
52,25
31,6
0,59
11,64
56,17
18,4
54,12
40,59
18,44
64,29
48,8
42,4
56,38
32,12
47,46
0,35
28,39
63,40
37,66
48,64
56,65
52,19
0,10
12,32
34,28
12,10
6,42
12,44
42,28
6,54
38,7
48,24
23,70
18,47
18,36
12,16
0,70
54,54
22,57
42,6
66,16
40,64
53,2
56,11
0,33
56,18
38,52
33,22
49,38
54,67
12,35
2,66
2,32
8,55
1,16
6,12
6,9
68,57
49,52
16,53
62,68
10,48
8,24
58,36
31,42
11,16
66,40
30,46
47,64
52,70
0,45
45,66
41,38
58,12
28,40
0,9
58,17
63,10
17,68
60,58
47,8
8,46
52,22
35,70
28,66
60,6
58,20
68,41
42,34
40,70
53,28
0,13
56,28
14,33
40,9
17,66
32,14
55,18
52,18
6,50
62,36
60,69
11,38
20,1
10,38
38,37
23,30
70,66
58,46
46,36
43,8
30,10
4,3
18,46
60,62
0,63
48,59
60,44
48,50
0,69
63,70
46,22
50,7
60,52
10,56
48,40
7,62
48,43
20,3
0,6
20,32
48,20
59,56
61,46
10,51
15,22
24,54
54,18
55,30
10,2
26,17
52,37
44,58
36,4
34,70
32,36
68,25
40,36
32,2
34,57
20,4
64,40
2,2
12,42
44,37
70,52
20,38
56,57
62,59
22,17
53,20
32,34
70,18
66,60
22,69
13,6
51,12
45,48
49,6
21,20
19,10
44,4
40,22
14,55
2,60
17,56
37,64
44,26
66,41
25,32
37,34
8,65
30,27
48,4
31,8
31,46
45,14
0,16
52,46
45,56
60,65
63,20
64,2
35,12
36,20
20,66
62,26
24,10
12,2
23,42
45,32
0,40
45,30
4,66
70,63
9,30
40,60
64,20
28,10
68,23
38,50
54,4
12,69
26,48
48,56
2,64
0,65
52,36
2,19
38,21
12,47
53,42
40,27
3,52
42,49
54,42
46,24
15,66
68,66
49,46
25,0
26,3
36,39
44,36
66,68
29,12
4,44
19,0
20,7
20,12
48,21
38,36
24,26
24,58
22,60
8,50
4,42
60,4
17,14
54,65
25,52
70,56
32,51
40,16
60,57
67,50
28,16
53,38
68,24
60,32
12,68
28,54
17,30
68,28
46,12
2,45
6,56
70,36
26,14
48,48
60,50
14,59
29,24
40,38
15,40
10,37
16,64
43,54
61,42
46,70
70,44
5,14
63,50
61,30
7,20
66,39
56,68
1,70
26,16
22,6
50,62
47,16
58,57
26,32
26,2
47,70
2,38
59,36
0,58
54,36
12,66
4,14
50,32
6,2
12,37
31,34
64,56
48,25
26,8
47,2
55,62
56,47
60,30
38,10
2,18
50,15
23,48
59,44
16,36
56,54
58,27
16,44
42,8
33,50
58,63
6,67
17,22
38,57
18,29
42,3
66,33
3,14
50,49
16,11
70,67
60,5
32,16
54,56
56,36
34,26
27,22
17,2
9,36
23,22
6,3
48,51
44,30
14,26
46,28
21,14
7,22
55,48
44,61
56,52
66,70
9,2
16,66
10,24
28,3
28,14
64,33
54,66
53,62
3,56
0,27
44,70
69,52
63,36
19,22
0,47
12,6
57,70
1,6
45,64
62,58
0,37
54,31
62,0
57,6
48,58
40,58
46,8
36,42
30,48
21,24
6,62
29,34
42,67
14,32
30,22
51,2
3,2
40,23
52,0
57,16
22,63
48,9
42,32
1,38
44,64
3,64
64,52
70,60
64,38
8,40
8,8
30,16
28,44
0,1
52,34
66,25
39,4
18,22
22,16
26,15
27,58
28,18
29,36
46,68
68,58
37,58
44,34
54,57
29,50
8,0
52,54
2,30
32,57
57,28
40,28
54,64
16,0
66,44
54,70
67,60
23,2
29,40
16,52
56,4
26,39
12,59
28,19
12,64
3,68
48,34
68,27
16,41
32,38
"""

# data = """
# 5,4
# 4,2
# 4,5
# 3,0
# 2,1
# 6,3
# 2,4
# 1,5
# 0,6
# 3,3
# 2,6
# 5,1
# 1,2
# 5,5
# 2,5
# 6,5
# 1,4
# 0,4
# 6,4
# 1,1
# 6,1
# 1,0
# 0,5
# 1,6
# 2,0
# """
size = 70

class Node:
    def __init__(self, position, end, parrent = None):
        self.parrent = parrent
        self.position = position

        if parrent != None:
            self.cost = parrent.cost + 1 
        else:
            self.cost = 0
        self.distance = abs(end - self.position)
    
    def fullCost(self): return self.cost + self.distance
    
    def __str__(self): return f"{self.position.real}, {self.position.imag}"
    def __hash__(self): return hash(str(self))
    def __eq__(self, other): 
        if other == None:
            return False
        else:
            return self.position   == other.position
    def __lt__(self, other): return self.fullCost() <  other.fullCost()
    def __gt__(self, other): return self.fullCost() >  other.fullCost()
    def __ge__(self, other): return self.fullCost() >= other.fullCost()
    def __le__(self, other): return self.fullCost() <= other.fullCost()

def draw(size, positions, blocks):
    for y in range(size):
        row = ""
        for x in range(size):
            if re.search(f"\n{x},{y}\n", blocks):
                row += "#"
            elif x+y*1j in positions:
                row += "O"
            else:
                row += "."
        print(row)

def aStar(data, size):
    start = Node(0+0j, size+size*1j)
    end = Node(size+size*1j, size+size*1j)
    opened = {str(start): start}
    closed = set()

    while len(opened) != 0:
        node = min(opened.values())
    
        closed.add(node)
        opened.pop(str(node))

        if node == end:
            path = []
            current = node
            while current != None:
                path.append(current.position)
                current = current.parrent
            return path

        for i in [1+0j, 0+1j, -1+0j, 0-1j]:
            newPos = node.position + i
            # collision
            if re.search(f"\n{int(newPos.real)},{int(newPos.imag)}\n", data) != None or newPos.real < 0 or newPos.real > size or newPos.imag < 0 or newPos.imag > size:
                continue

            child = Node(newPos, end.position, node)

            if child in closed:
                continue

            if str(child) in opened:
                if opened[str(child)] > child:
                    opened[str(child)] = child
            else:
                opened[str(child)] = child

    return None

n = 2000
blocks = "\n".join(data.split("\n")[:n]) + "\n"
path = aStar(blocks, size)
while path != None:
    new = data.split("\n")[n]
    x,y = new.split(",")
    n += 1
    if int(x)+int(y)*1j not in path:
        blocks = blocks + new + "\n"
        continue
    else:
        blocks = blocks + new + "\n"
        path = aStar(blocks, size)
        print(n)
print(new)
#draw(size, path, blocks)