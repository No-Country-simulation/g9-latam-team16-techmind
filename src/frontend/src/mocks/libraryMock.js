export const libraryMock = [
  {
    id: 1,
    title: "Fundamentos de React Hooks",
    summary:
      "Aprende a utilizar React Hooks para manejar estado y efectos secundarios en componentes funcionales. Incluye ejemplos prácticos con useState, useEffect y useContext.",
    category: "Programación",
    subcategory: "React",
    type: "Text",
    confidence: 92,
    keywords: ["React", "Hooks", "JavaScript", "Frontend"],
    createdAt: "2024-01-15",
  },
  {
    id: 2,
    title: "Guía Completa de Material UI",
    summary:
      "Domina Material UI con esta guía completa que cubre componentes, temas personalizados, sistema de estilos sx y buenas prácticas. Perfecto para diseñar interfaces profesionales.",
    category: "Diseño",
    subcategory: "Componentes UI",
    type: "File",
    confidence: 88,
    keywords: ["Material UI", "Diseño", "CSS", "React"],
    createdAt: "2024-01-20",
  },
  {
    id: 3,
    title: "Node.js y Express: Backend Moderno",
    summary:
      "Construye servidores backend escalables con Node.js y Express. Cubre rutas, middleware, manejo de errores y conexión a bases de datos.",
    category: "Programación",
    subcategory: "Backend",
    type: "File",
    confidence: 85,
    keywords: ["Node.js", "Express", "Backend", "API REST"],
    createdAt: "2024-01-25",
  },
  {
    id: 4,
    title: "Bases de Datos con MongoDB",
    summary:
      "Introducción a MongoDB: instalación, operaciones CRUD, aggregation pipeline y optimización de consultas. Incluye patrones de diseño para aplicaciones modernas.",
    category: "Base de Datos",
    subcategory: "NoSQL",
    type: "Text",
    confidence: 90,
    keywords: ["MongoDB", "Base de Datos", "NoSQL", "Queries"],
    createdAt: "2024-02-01",
  },
  {
    id: 5,
    title: "Testing con Jest y React Testing Library",
    summary:
      "Aprende a escribir pruebas unitarias y de integración para componentes React. Cubre mocking, snapshots y mejores prácticas de testing.",
    category: "Calidad",
    subcategory: "Testing",
    type: "Text",
    confidence: 87,
    keywords: ["Jest", "Testing", "React", "QA"],
    createdAt: "2024-02-05",
  },
  {
    id: 6,
    title: "DevOps y Deployment en AWS",
    summary:
      "Guía práctica de DevOps: CI/CD, Docker, Kubernetes y deployment en AWS. Automatiza tu pipeline de desarrollo para entregas más rápidas y confiables.",
    category: "DevOps",
    subcategory: "Cloud",
    type: "File",
    confidence: 94,
    keywords: ["AWS", "DevOps", "Docker", "CI/CD", "Deployment"],
    createdAt: "2024-02-10",
  },
];

export const getCategoriesFromMock = () => {
  return Array.from(new Set(libraryMock.map((item) => item.category))).sort();
};

export const getSubcategoriesFromMock = (category) => {
  return Array.from(
    new Set(
      libraryMock
        .filter((item) => item.category === category)
        .map((item) => item.subcategory),
    ),
  ).sort();
};

export const getContentTypesFromMock = () => {
  return Array.from(new Set(libraryMock.map((item) => item.type))).sort();
};
