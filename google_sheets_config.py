"""
Google Sheets에서 API 키를 가져오는 모듈
Git에 API 키를 노출하지 않고 안전하게 관리
"""

import requests
import json
import os

class GoogleSheetsConfig:
    def __init__(self, sheet_id, sheet_name="key", column="A", row=1):
        """
        Google Sheets에서 설정을 가져오는 클래스
        
        Args:
            sheet_id: Google Sheets ID
            sheet_name: 시트 이름 (기본값: "key")
            column: 열 (기본값: "A")
            row: 행 (기본값: 1)
        """
        self.sheet_id = sheet_id
        self.sheet_name = sheet_name
        self.column = column
        self.row = row
        self.api_key = None
        
    def get_api_key(self):
        """Google Sheets에서 API 키를 가져옵니다"""
        try:
            # Google Sheets 공개 URL (CSV 형식)
            url = f"https://docs.google.com/spreadsheets/d/{self.sheet_id}/export?format=csv&gid=0"
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # CSV 데이터 파싱
            lines = response.text.strip().split('\n')
            if len(lines) > 0:
                # 첫 번째 행의 첫 번째 열 데이터 추출
                first_line = lines[0].strip()
                # CSV 형식에서 따옴표 제거
                api_key = first_line.strip('"').strip("'")
                self.api_key = api_key
                return api_key
            else:
                raise ValueError("API 키를 찾을 수 없습니다.")
                
        except Exception as e:
            print(f"Google Sheets에서 API 키를 가져오는 중 오류 발생: {str(e)}")
            # 백업: 환경 변수에서 가져오기
            return os.getenv("OPENAI_API_KEY", "")
    
    def get_config(self):
        """설정 정보를 반환합니다"""
        if not self.api_key:
            self.api_key = self.get_api_key()
        
        return {
            "openai_api_key": self.api_key,
            "source": "google_sheets"
        }

# 사용 예시
def get_openai_api_key():
    """OpenAI API 키를 가져옵니다"""
    # Google Sheets ID (URL에서 추출)
    sheet_id = "1CLaPh3ACxgx4JNBgAOgXtuYhKApMTH2MF9vjyStv_XI"
    
    config = GoogleSheetsConfig(sheet_id)
    return config.get_api_key()

if __name__ == "__main__":
    # 테스트
    api_key = get_openai_api_key()
    print(f"API 키: {api_key[:10]}..." if api_key else "API 키를 가져올 수 없습니다.")
