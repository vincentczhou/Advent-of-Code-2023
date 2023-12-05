package org.adventofcode2023;

import lombok.SneakyThrows;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;

public class PartTwo {

    public static int numMatches (String[] winCard, String[] myCard) {
        int matches = 0;
        for (String num : myCard) {
            for (String winNum: winCard) {
                if (num.equals(winNum)) {
                    matches++;
                    break;
                }
            }
        }
        return matches;
    }

    public static int parseLine(String line) {
        String[] chunk = line.split(":");
        String[] cardSet = chunk[1].split("\\|");
        String[] winCard = cardSet[0].trim().split(" +");
        String[] myCard = cardSet[1].trim().split(" +");

        return numMatches(winCard, myCard);
    }

    public static void main(String[] args) {
        var input = getInput("input");

        String[] inputLines = input.split("\n");
        int[] cardsMatches = new int[inputLines.length];
        int[] cardCopies = new int[inputLines.length];
        Arrays.fill(cardCopies, 1);
        for (int i = 0; i < inputLines.length; i++) {
            cardsMatches[i] = parseLine(inputLines[i]);
        }

        for (int i = 0; i < cardsMatches.length; i++) {
            for (int j = 0; j < cardsMatches[i]; j++) {
                cardCopies[i + j + 1] += cardCopies[i];
            }
        }

        int sum = 0;
        for (int copy : cardCopies) {
            sum += copy;
        }
        
        System.out.printf("The sum is: %s", sum);
    }

    @SneakyThrows
    @SuppressWarnings({"SameParameterValue", "DataFlowIssue"})
    private static String getInput(String fileName) {
        return Files.readString(Paths.get(Main.class.getClassLoader().getResource(fileName).toURI())).trim();
    }
}