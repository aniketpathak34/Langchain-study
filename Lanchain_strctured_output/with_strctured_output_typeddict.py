from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation"
)
chatmodel = ChatHuggingFace(llm=llm)


class Review(TypedDict):
    key_themes: Annotated[list[str], "A list of the main themes discussed in the review."]
    summary: Annotated[str, "A brief summary of the review."]
    sentiment: Annotated[str, "The overall sentiment of the review, e.g., positive, negative, neutral."]
    pros: Annotated[Optional[list[str]], "A list of positive aspects mentioned in the review."]
    cons: Annotated[Optional[list[str]], "A list of negative aspects mentioned in the review."]

structured_model = chatmodel.with_structured_output(Review)


result = structured_model.invoke("""The software offers an impressive blend of usability, performance, and thoughtful design. Its clean interface makes navigation effortless, while automation tools noticeably boost productivity and reduce repetitive work. Regular updates and responsive customer support show genuine attention to user needs.

Performance remains stable even under heavy workloads, and the overall experience feels smooth and professional. However, advanced users may find customization options slightly limited, and integration with certain third-party platforms could be broader.

Overall, it leaves a strongly positive impression, combining simplicity, reliability, and speed in a way that enhances everyday efficiency.""")


print(result)