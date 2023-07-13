package search.pattern;

public class PatternSearch {
    public static void patternSearch(String text, String pattern) {
        System.out.println("Input Text: " + text + " Input Pattern: " + pattern);
        
        for (int index = 0; index < text.length(); index++) {
            System.out.println("Text Index: " + index);
            int matchCount = 0;
            
            for (int charIndex = 0; charIndex < pattern.length(); charIndex++) {
                System.out.println("Pattern Index: " + charIndex);
                
                if (pattern.charAt(charIndex) == text.charAt(index + charIndex)) {
                    matchCount++;
                } else {
                    break;
                }
            }
            
            if (matchCount == pattern.length()) {
                System.out.println(pattern + " found at index " + index);
            }
        }
    }
    
    public static void main(String[] args) {
        String text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE";
        String pattern = "NEEDLE";
        patternSearch(text, pattern);
        
        // New inputs to test
        String text2 = "SOMEMORERANDOMWORDSTOpatternSEARCHTHROUGH";
        String pattern2 = "pattern";
        patternSearch(text2, pattern2);
        
        String text3 = "This   still      works with    spaces";
        String pattern3 = "works";
        patternSearch(text3, pattern3);
        
        String text4 = "722615457824612704202682179992552072047396";
        String pattern4 = "42";
        patternSearch(text4, pattern4);
    }
}
