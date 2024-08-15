from fastapi import APIRouter, File, UploadFile, HTTPException, Form
import pandas as pd
import shutil
import os

router = APIRouter()

UPLOAD_DIRECTORY = "frontend/uploads"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@router.post("/uploadfiles/")
async def upload_files(file1: UploadFile = File(...), file2: UploadFile = File(...), file3: UploadFile = File(...)):
    files = [file1, file2, file3]
    for file in files:
        file_location = f"{UPLOAD_DIRECTORY}/{file.filename}"
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)
    return {"message": "Files uploaded successfully"}

@router.get("/user/{matricule}")
def get_user(matricule: int):
    try:
        # Log to check if the files exist
        print(f"Reading files from {UPLOAD_DIRECTORY}")
        df1_path = os.path.join(UPLOAD_DIRECTORY, 'fichier1.xlsx')
        df2_path = os.path.join(UPLOAD_DIRECTORY, 'fichier2.xlsx')
        df3_path = os.path.join(UPLOAD_DIRECTORY, 'fichier3.xlsx')
        
        if not os.path.exists(df1_path):
            raise HTTPException(status_code=404, detail="fichier1.xlsx not found")
        if not os.path.exists(df2_path):
            raise HTTPException(status_code=404, detail="fichier2.xlsx not found")
        if not os.path.exists(df3_path):
            raise HTTPException(status_code=404, detail="fichier3.xlsx not found")

        df1 = pd.read_excel(df1_path)
        df2 = pd.read_excel(df2_path)
        df3 = pd.read_excel(df3_path)
        
        print(f"df1 head: {df1.head()}")
        print(f"df2 head: {df2.head()}")
        print(f"df3 head: {df3.head()}")
        print(f"df1 columns: {df1.columns}")
        print(f"df2 columns: {df2.columns}")
        print(f"df3 columns: {df3.columns}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading files: {str(e)}")

    try:
        print(f"Searching for matricule {matricule}")
        user_info1 = df1[df1['matricule'] == matricule]
        if user_info1.empty:
            print("User not found in fichier1.xlsx")
            raise HTTPException(status_code=404, detail="User not found in fichier1.xlsx")
        else:
            print(f"User info found in fichier1.xlsx: {user_info1}")

        numero_affiliation = user_info1['numero_affiliation'].values[0]
        date_cotisation = user_info1['date_cotisation'].values[0]

        user_info2 = df2[df2['matricule'] == matricule]
        nombre_mois = user_info2.shape[0]

        user_info3 = df3[df3['matricule'] == matricule]
        if user_info3.empty:
            a_avance = "Non"
        else:
            a_avance = user_info3['a_avance'].values[0]

        return {
            "matricule": matricule,
            "numero_affiliation": numero_affiliation,
            "date_cotisation": date_cotisation,
            "nombre_mois": nombre_mois,
            "a_avance": a_avance
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing user data: {str(e)}")
@router.put("/user/{matricule}")
def update_telephone(matricule: int, telephone: str = Form(...)):
    try:
        df1_path = os.path.join(UPLOAD_DIRECTORY, 'fichier1.xlsx')
        if not os.path.exists(df1_path):
            raise HTTPException(status_code=404, detail="fichier1.xlsx not found")

        df1 = pd.read_excel(df1_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading files: {str(e)}")

    try:
        user_index = df1.index[df1['matricule'] == matricule].tolist()
        if not user_index:
            raise HTTPException(status_code=404, detail="User not found in fichier1.xlsx")

        df1.at[user_index[0], 'telephone'] = telephone
        df1.to_excel(df1_path, index=False)

        return {"message": "Telephone number updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating user data: {str(e)}")