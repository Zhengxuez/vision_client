package main;

import scene.service.SceneClient;

public class Application {
    public static void main(String[] args) {
        SceneClient client = new SceneClient();

        // Dynamically specify the question
        String question = "What is the main object in the scene?";

        try {
            // Call the describeScene method with the custom question
            String result = client.describeScene(question);
            System.out.println("Scene Description:");
            System.out.println(result);
        } catch (Exception e) {
            System.err.println("An error occurred:");
            e.printStackTrace();
        }
    }
}
