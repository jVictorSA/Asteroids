#include <iostream>
#include <GL/glew.h>
#include <GL/freeglut.h>
#include <stdio.h>
#include "Include/ogldev_math_3d.h"

using namespace std;
GLuint VBO;


class SpaceShip{
	private:
		Vector3f vert[3]; //dimensions to draw
		float vert_translate[2]; //translations
		float delta_pos[2]; //deta translations
	public:
		SpaceShip(){
			vert[0] = Vector3f(0.0f, 0.06f, 0.0f); ///top
			vert[1] = Vector3f(0.02f, -0.02f, 0.0f); //botton left
			vert[2] = Vector3f(-0.02f, -0.02f, 0.0f); //botton right
			vert_translate[0] = 0.0f;
			vert_translate[1] = 0.0f;
			delta_pos[0]=0.01f;
			delta_pos[1]=0.01f;
			printf("Ship created.\n");
		}

		void Keyboard(unsigned char key, int x, int y){
			if ((key=='w') || (key=='W')){
				cout << "UP" << endl;
				if (vert_translate[0]<1)
				{vert_translate[0] += delta_pos[0];}
			}
		}

		void Translate(){
			glutKeyboardFunc(Keyboard);
		}

		Vector3f* GetVector(){return vert;}
};


static void RenderSceneCB(){
    glClear(GL_COLOR_BUFFER_BIT);

	glBindBuffer(GL_ARRAY_BUFFER, VBO);
	glEnableVertexAttribArray(0);
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0);
	glDrawArrays(GL_TRIANGLES, 0, 3);
	glDisableVertexAttribArray(0);

    glutSwapBuffers();
}


static void CreateVertexBuffer(SpaceShip ship){
	Vector3f vertices[3];
	vertices[0] = ship.GetVector()[0];
	vertices[1] = ship.GetVector()[1];
	vertices[2] = ship.GetVector()[2];

	glGenBuffers(1, &VBO);
	glBindBuffer(GL_ARRAY_BUFFER, VBO);
	glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
}


int main(int argc, char **argv){

    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGBA);

    int width = 1080;
    int height = 700;
    glutInitWindowSize(width, height);

    int x = 100;
    int y = 10;
    glutInitWindowPosition(x, y);
    int win = glutCreateWindow("Asteroids");
    cout<<"Window: "<<win<<endl;

	GLenum res;
	res = glewInit();
	if (res!=GLEW_OK){
		cout << "Error: " << gluErrorString(res) << endl;
		return 1;
	}

    GLclampf red, green, blue, alpha;
    red = green = blue = alpha = 0.0f;
    glClearColor(red, green, blue, alpha);

	SpaceShip ship;
	ship.Translate();

	CreateVertexBuffer(ship);

    glutDisplayFunc(RenderSceneCB);
	//glutDisplayFunc(ship.LoopRenderSpaceShip);

    glutMainLoop();

    return 0;
}