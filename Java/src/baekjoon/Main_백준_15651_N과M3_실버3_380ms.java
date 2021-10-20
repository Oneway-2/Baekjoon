package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_백준_15651_N과M3_실버3_380ms {
	static int N, M, numbers[];
	private static StringBuilder sb;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		sb = new StringBuilder();
		N = Integer.parseInt(stk.nextToken());
		M = Integer.parseInt(stk.nextToken());
		numbers = new int[M];
		per(0);
		System.out.println(sb);
	} // 메인 끝

	private static void per(int cnt) {
		//중복순열
		if (cnt == M) {
			for (int i = 0; i < numbers.length; i++) {
				sb.append(numbers[i]).append(" ");
			}
			sb.append("\n");
			return;
		}
		for (int i = 1; i <= N; i++) {
			numbers[cnt] = i;
			per(cnt + 1);
		}
	}
}
