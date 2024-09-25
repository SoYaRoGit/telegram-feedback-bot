from sqlalchemy import BigInteger, Column, Integer, String, Text

from database.database import Base


class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    user_telegram_id = Column(BigInteger, unique=False, nullable=False)
    user_name = Column(String)
    text_feedback = Column(Text, nullable=False)

    def __repr__(self):
        return (
            f"<Feedback(id={self.id}, "
            f"user_telegram_id={self.user_telegram_id}, "
            f"user_name='{self.user_name}', "
            f"text_feedback='{self.text_feedback[:20]}...')>"
        )
