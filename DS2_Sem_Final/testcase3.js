import * as functions from "firebase-functions";
import {Configuration, OpenAIApi} from "openai";

// // Start writing functions
// // https://firebase.google.com/docs/functions/typescript
//
// export const helloWorld = functions.https.onRequest((request, response) => {
//   functions.logger.info("Hello logs!", {structuredData: true});
//   response.send("Hello from Firebase!");
// });

// Config => API Key
const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});

// OpenAI
const openai = new OpenAIApi(configuration);


export const aiChatbot = functions.https.onRequest(async (request, response) => {
  const params = request.query;

  if (!params.query) {
    response.send("Internal Error: No query parameter specified");
  }

  const openAIAPIResponse = await openai.createCompletion({
    model: "text-davinci-003",
    prompt: params?.query?.toString() || "Not defined",
    temperature: 1,
    max_tokens: 500,
    top_p: 1,
    frequency_penalty: 0,
    presence_penalty: 0.6,
    stop: [" Human:", " AI:"],
  });

  response.send(JSON.stringify(openAIAPIResponse.data));
});