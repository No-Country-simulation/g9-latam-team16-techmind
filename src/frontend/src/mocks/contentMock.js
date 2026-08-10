export async function registerTextMock(request) {
  console.log("Mock request:", request);

  return Promise.resolve({
    id: crypto.randomUUID(),

    title: request.title,

    category: "Backend",

    subcategory: "Spring Boot",

    confidence: 0.96,

    keywords: ["java", "spring", "rest"],

    createdAt: new Date().toISOString(),
  });
}
