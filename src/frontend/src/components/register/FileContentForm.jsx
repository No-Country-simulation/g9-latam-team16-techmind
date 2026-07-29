import { Typography } from "@mui/material";

function FileContentForm() {
  const [file, setFile] = useState(null);

  const [loading, setLoading] = useState(false);
  const [classification, setClassification] = useState(null);
  const handleSubmit = async () => {
    try {
      setLoading(true);

      const request = createRegisterTextRequest(title, content);
      const response = await registerText(request);

      console.log(response);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };
  return;
  <Button
    variant="contained"
    onClick={handleSubmit}
    disabled={!content.trim() || loading}
  >
    {loading ? "Clasificando..." : "Clasificar contenido"}
  </Button>;
}

export default FileContentForm;
