/* Includes */

//#include "../inc/NanoEdgeAI.h"
//#include "../inc/knowledge.h"

#include <stdlib.h>
#include <stdio.h>

/* Define */

#define AXIS_NUMBER 3
#define DATA_INPUT_USER 128
#define CLASS_NUMBER 6

void affiche (const float *tableau, int length);
void affiche_int (const int *tableau, int length);
int lines(FILE* fichier);

/* Main */

int main(int argc, char const *argv[])
{
	printf("Start\n");
	FILE* data = fopen("../datas/test/dataset_studio/data_1.txt", "r");
	printf("File opened\n");

	/* Initialization */
	//int error_code = NanoEdgeAI_knowledge_init(knowledge);

	//if (error_code != 0)
	//{
		/* This happen if the knowledge is not loaded. */
		//printf("Error : the knowledge haven't been correctly loaded.\n");

	//}

	/* Classification */
	const int nb_lines = lines(data);
	printf("%d \n", nb_lines);
	int id_class[nb_lines];
	//affiche_int(id_class, nb_lines);
	for (int line=0; line<3; line++)
	{
		printf("line : %d \n", line);
		float knowledge_buffer[DATA_INPUT_USER * AXIS_NUMBER];
		
		fscanf(data, "%f %f %f", &knowledge_buffer[0], &knowledge_buffer[1], &knowledge_buffer[2]);
		printf("acc_x : %f ; acc_y : %f ; acc_z : %f \n", knowledge_buffer[0], knowledge_buffer[1], knowledge_buffer[2]);
		/*for (int i=0; i<DATA_INPUT_USER*AXIS_NUMBER; i++)
		{
			//fscanf(data, "%f %f %f", &knowledge_buffer[3*i], &knowledge_buffer[3*i+1], &knowledge_buffer[3*i+2]);
			//printf("acc_x : %f ; acc_y : %f ; acc_z : %f \n", knowledge_buffer[3*i], knowledge_buffer[3*i+1], knowledge_buffer[3*i+2]);
			fscanf(data, "%f ", &knowledge_buffer[i]);
			printf("acc : %f ", knowledge_buffer[i]);
		}
		printf("\n\n");*/
		//id_class[line] = NanoEdgeAI_classifier(input_user_buffer, output_class_buffer, 0);
	}
	fclose(data);
	return 0;
}

void affiche (const float *tableau, int length)
{
     int i;
     for (i = 0; i < length; ++i)
     {
        printf("tableau [%d] = %f \n", i, tableau[i]);
     }
 
 }

void affiche_int (const int *tableau, int length)
{
     int i;
     for (i = 0; i < length; ++i)
     {
        printf("tableau [%d] = %d \n", i, tableau[i]);
     }
 
 }

 int lines(FILE* fichier)
 {
 	int c_1;
 	int c_2;
 	int nb_line = 0;
 	while ((c_1=fgetc(fichier)) != EOF)
 	{
 		if (c_1=='\n')
 		{
 			nb_line++;
 		}
 		c_2 = c_1;
 	}
 	if(c_2 != '\n')
 	{
 		nb_line++;
 	}

 	return nb_line;
 }