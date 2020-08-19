package com.noob;

import java.util.*;

public class Tictactoe {

    static ArrayList<Integer> playerPositions = new ArrayList<Integer>();
    static ArrayList<Integer> botPositions = new ArrayList<Integer>();

    public static void main(String[] args) {

        char[][] playground = {{'-', '-', '-', '-', '-', '-', '-' },
                {'|', ' ', '|', ' ', '|', ' ', '|' },
                {'-', '-', '-', '-', '-', '-', '-' },
                {'|', ' ', '|', ' ', '|', ' ', '|' },
                {'-', '-', '-', '-', '-', '-', '-' },
                {'|', ' ', '|', ' ', '|', ' ', '|' },
                {'-', '-', '-', '-', '-', '-', '-' }};

        printground(playground);

        while (true) {

            Scanner scan = new Scanner(System.in);
            System.out.println("Which room you choose (1-9): ");
            int play_opt = scan.nextInt();
            while(playerPositions.contains(play_opt) || botPositions.contains(play_opt)) {
                System.out.println("Position taken");
                play_opt = scan.nextInt();
            }

            placing_opt(playground, play_opt, "player");

            String result = checkWinner();
            if(result.length() > 0) {
                System.out.println(result);
                break;
            }

            Random rand = new Random();
            int bot_opt = rand.nextInt(9) + 1;
            while(playerPositions.contains(bot_opt) || botPositions.contains((bot_opt))) {
                bot_opt = rand.nextInt(9) + 1;
            }

            placing_opt(playground, bot_opt, "bot");

            printground(playground);

            result = checkWinner();
            if(result.length() > 0) {
                System.out.println(result);
                break;
            }

        }

    }

    public static void printground(char[][] playground) {
        for (char[] row : playground) {
            for (char x : row) {
                System.out.print(x);
            }
            System.out.println();
        }
    }

    public static void placing_opt(char[][] playground, int play_opt, String user) {
        char place = ' ';
        if (user.equals("player")) {
            place = 'x';
            playerPositions.add(play_opt);
        } else if (user.equals("bot")) {
            place = 'o';
            botPositions.add(play_opt);
        }

        switch (play_opt) {
            case 1:
                playground[1][1] = place;
                break;
            case 2:
                playground[1][3] = place;
                break;
            case 3:
                playground[1][5] = place;
                break;
            case 4:
                playground[3][1] = place;
                break;
            case 5:
                playground[3][3] = place;
                break;
            case 6:
                playground[3][5] = place;
                break;
            case 7:
                playground[5][1] = place;
                break;
            case 8:
                playground[5][3] = place;
                break;
            case 9:
                playground[5][5] = place;
                break;
            default:
                break;
        }
    }

    public static String checkWinner() {

        List topRow = Arrays.asList(1, 2, 3);
        List midRow = Arrays.asList(4, 5, 6);
        List undRow = Arrays.asList(7, 8, 9);
        List leftcol = Arrays.asList(1, 4, 7);
        List midcol = Arrays.asList(2, 5, 8);
        List rigcol = Arrays.asList(3, 6, 9);
        List cross_1 = Arrays.asList(1, 5, 9);
        List cross_2 = Arrays.asList(7, 5, 3);

        List<List> winCheck = new ArrayList<List>();
        winCheck.add(topRow);
        winCheck.add(midRow);
        winCheck.add(undRow);
        winCheck.add(leftcol);
        winCheck.add(midcol);
        winCheck.add(rigcol);
        winCheck.add(cross_1);
        winCheck.add(cross_2);

        for (List l : winCheck) {
            if (playerPositions.containsAll(l)) {
                return "You win";
            } else if (botPositions.containsAll(l)) {
                return "You lose";
            } else if (playerPositions.size() + botPositions.size() == 9) {
                return "Tie!!";
            }
        }
    return "";
    }

}